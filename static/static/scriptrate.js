(function($) {


  // Make elements equal to the viewport height. 
  // Or at least as tall as the viewport height, if second parameter is true. Sets the 'height' or 'min-height' property.
	function setToViewportHeight( selector, forceViewportMax )
  {
		var viewportHeight = $(window).innerHeight();

		$(selector).each(function(){
			var height = $(this).height();

      if ( forceViewportMax == true ){
        // Set height to same as viewport height.
        if ( height < viewportHeight ){
          $(this).height(viewportHeight);
        }  
      } 
      else {
        // Min height of element that is the same as the viewport
        $(this).css('min-height', viewportHeight + "px");
      }

		});
	}
  
  // Reverse scroll of the middle column in the Image Column Grid.
  //   (Organized within the "module pattern": self-executes an 
  //    anonymous function that returns an object) 
  var reverseScroll = (function(){
    
    var selector = '.image-column-grid .reverse';
    var selectorNotReverse = '.image-column-grid .column:not(.reverse)';
    var wrapSelector = '.image-column-grid';
    // Number of column pixels always visible, until scrolling begins
    var fixedOffsetEdge = 180; 
    
    var setupBindings = function(){
      
      // Regular column element(s)
  $(selectorNotReverse).each(function(index, el){
        var startOffset = window.innerHeight - fixedOffsetEdge;
        $(el).css('margin-top', startOffset+"px");
      });
      
      // Reversed column element(s)
      $(selector).each(function(index, el){
          // Get container
          var container = $(el).closest(wrapSelector);
          if ( $(container).length == 0){ return; }
        
          // Get heights
          var wrapHeight = $(container).outerHeight();
          var elHeight = $(el).outerHeight();
          var firstChildHeight = $('*:first-child', el).outerHeight();
          var lastChildHeight = $('*:last-child', el).outerHeight();
        
          // Total amount that margin changes (top to bottom of scroll) 
          // And don't scroll past last item (first child)
          var scrollTotal = (wrapHeight + elHeight) -firstChildHeight - fixedOffsetEdge;

          // Set a negative top value to move it out of sight.
          $(el).css('top', (-elHeight + fixedOffsetEdge) + "px");

          // When scrolling, change margin proportionately.
          $(window).on('scroll', function(){
            // Any part of element enters viewport
            if ( isScrolledIntoView( $(container)[0], false) && wrapHeight > 0 )
            {
              // Start scrolling when this point is reached
              var scrollStart = window.innerHeight;
              
              // Where element is offset from top of the page. 
              // If it's visible on load, the starting scroll point 
              // starts there, rather than when element comes into view.
              var containerOffset = $(container).offset().top;
              //console.log(containerOffset);
              if (containerOffset < window.innerHeight){
                scrollStart = window.innerHeight - containerOffset;
              }
              //console.log("scrollStart:"+scrollStart);
              
              // Where top of container is scrolled to in the window
              var elemTop = $(container)[0].getBoundingClientRect().top;

              // Percent scaled ratio (0 to 1.0)
              var minToStartScroll = fixedOffsetEdge;
              if (scrollStart > minToStartScroll){
                minToStartScroll = scrollStart;
              }
              var percentScrolled = (window.innerHeight - elemTop - minToStartScroll) / (wrapHeight - window.innerHeight + lastChildHeight + fixedOffsetEdge);
              //console.log("min to start scroll:"+minToStartScroll);
              console.log("percentScrolled: "+percentScrolled);
              if (percentScrolled < 0){ percentScrolled = 0; }
              if (percentScrolled > 1){ percentScrolled = 1.0; }

              // Scale total margin change by percent scrolled.
              var newMargin = (scrollTotal * percentScrolled);
              // Set new margin
              $(el).css('transform', 'translateY(' + newMargin + 'px)');
            }
          });

        });
      
    } // end setupBindings
    
    var init = function(){
      setupBindings();
    }
    
    // Public API
    return {
        init: init
    };
  })();
  

  // Check if element is scrolled into view.
  // Pass true to "fullyInView" if the whole element must be visible
  function isScrolledIntoView(el, fullyInView) {
    var elemTop = el.getBoundingClientRect().top;
    var elemBottom = el.getBoundingClientRect().bottom;
    var isVisible = false;

    if (fullyInView == true){
      // element must be fully within viewport
      isVisible = (elemTop >= 0) && (elemBottom <= window.innerHeight);
    } else {
      // any part of element is visible in the viewport
      isVisible = elemTop <= window.innerHeight;
    }
    return isVisible;
  }
  
  // INIT
  setToViewportHeight('.viewport-height', false);
  reverseScroll.init();
  
  // Window Resize
  // To-Do/Should Do: debounce
  $(window).resize(function() {
    setToViewportHeight('.viewport-height', false);
    reverseScroll.init();
    //console.log('resize');
  });
  
})(jQuery);