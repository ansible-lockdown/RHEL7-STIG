// Toggle main sections
$(".docs-sidebar-section-title").click(function () {
    $('.docs-sidebar-section').not(this).closest('.docs-sidebar-section').removeClass('active');
    $(this).closest('.docs-sidebar-section').toggleClass('active');
// Bug #1422454
// Commenting out next line, the default behavior which was preventing links
// from working.
//    event.preventDefault();
});

/* Bug #1422454
   The toggle functions below enable the expand/collapse, but for now
   there's no easy way to get deeper links from other guides. So,
   commenting both toggle functions out.
// Toggle 1st sub-sections
$(".docs-sidebar-section ol lh").click(function () {
    $('.docs-sidebar-section ol').not(this).closest('.docs-sidebar-section ol').removeClass('active');
    $(this).closest('.docs-sidebar-section ol').toggleClass('active');
    if ($('.docs-has-sub').hasClass('active')) {
      $(this).closest('.docs-sidebar-section ol li').addClass('open');
    }
    event.preventDefault();
});

// Toggle 2nd sub-sections
$(".docs-sidebar-section ol > li > a").click(function () {
    $('.docs-sidebar-section ol li').not(this).removeClass('active').removeClass('open');
    $(this).closest('.docs-sidebar-section ol li').toggleClass('active');
    if ($('.docs-has-sub').hasClass('active')) {
      $(this).closest('.docs-sidebar-section ol li').addClass('open');
    }
    event.preventDefault();
});

/* Bug #1417291
   The rule below creates a shaded plus sign next to
   a numbered sublist of a bulleted list.
   It's probably there to implement expand/collapse of
   list items, but unfortunately it affects also those
   lists where expand/collapse is not intended.

   I am commenting it out to fix this bug. If it causes
   problems elsewhere, they have to be fixed elsewhere. */

// $('ol > li:has(ul)').addClass('docs-has-sub');

// webui popover
$(document).ready(function() {
    function checkWidth() {
        var windowSize = $(window).width();

        if (windowSize <= 767) {
            $('.gloss').webuiPopover({placement:'auto',trigger:'click'});
        }
        else if (windowSize >= 768) {
            $('.gloss').webuiPopover({placement:'auto',trigger:'hover'});
        }
    }

    // Execute on load
    checkWidth();
    // Bind event listener
    $(window).resize(checkWidth);
});

// Bootstrap stuff
$('.docs-actions i').tooltip();
$('.docs-sidebar-home').tooltip();

// Hide/Toggle definitions
$("#toggle-definitions").click(function () {
  $(this).toggleClass('docs-info-off');
  if ($('.gloss').hasClass('on')) {
      $('.gloss').removeClass('on').addClass('off').webuiPopover('destroy');
  } else if ($('.gloss').hasClass('off')) {
      $('.gloss').removeClass('off').addClass('on').webuiPopover();
  }
});

/* BB 150310
   openstackdocstheme provides three types of admonitions, important, note
   and warning. We decorate their title paragraphs with Font Awesome icons
   by adding the appropriate FA classes.                               */

$('div.important > p.admonition-title').prepend('<div class="fa fa-fw fa-check-circle">&nbsp;</div>');
$('div.note > p.admonition-title').prepend('<div class="fa fa-fw fa-check-circle">&nbsp;</div>');
$('div.seealso > p.admonition-title').prepend('<div class="fa fa-fw fa-info-circle">&nbsp;</div>');
$('div.warning > p.admonition-title').prepend('<div class="fa fa-fw fa-exclamation-triangle">&nbsp;</div>');
$('div.versionadded > p').prepend('<div class="fa fa-fw fa-plus-circle">&nbsp;</div>');
$('div.versionchanged > p').prepend('<div class="fa fa-fw fa-info-circle">&nbsp;</div>');
$('div.deprecated > p').prepend('<div class="fa fa-fw fa-minus-circle">&nbsp;</div>');

/* BB 150310
   We also insert a space between the icon and the admonition title
   ("Note", "Warning", "Important" or their i18n equivalents).

   This could be done with a single clause $('p.admonition-title')....,
   affecting all types of admonitions. I play it safe here and explicitly
   work on the three openstackdocstheme admonitions.

   The first parameter of the text() callback is not needed here (it's
   the index of the HTML element that we are modifying)                 */

// Gives the log a bug icon the information it needs to generate the bug in
// Launchpad with pre-filled information such as git SHA, git.openstack.org
// source URL, published document URL and tag.
function logABug(bugTitle, bugProject, fieldComment, fieldTags, repositoryName, useStoryboard) {

    var lineFeed = "%0A";

    var bugChecklist = "This bug tracker is for errors with the documentation, " +
        "use the following as a template and remove or add fields as " +
        "you see fit. Convert [ ] into [x] to check boxes:" + lineFeed + lineFeed +
        "- [ ] This doc is inaccurate in this way: ______" + lineFeed +
        "- [ ] This is a doc addition request." + lineFeed +
        "- [ ] I have a fix to the document that I can paste below including example: " +
        "input and output. " + lineFeed + lineFeed +
        "If you have a troubleshooting or support issue, use the following " +
        " resources:" + lineFeed + lineFeed +
        " - Ask OpenStack: http://ask.openstack.org" + lineFeed +
        " - The mailing list: http://lists.openstack.org" + lineFeed +
        " - IRC: 'openstack' channel on Freenode"+ lineFeed;

    var urlBase = "https://bugs.launchpad.net/" + bugProject + "/+filebug?field.title=";
    var currentURL = "URL: " + window.location.href;
    var bugLink = "";
    if (useStoryboard) {
        var urlBase = "https://storyboard.openstack.org/#!/project/";
        bugLink = urlBase + repositoryName;
    } else {
        bugLink = urlBase  + encodeURIComponent(bugTitle) +
        "&field.tags=" + fieldTags +
        "&field.comment=" + lineFeed + lineFeed +  lineFeed +
        bugChecklist + lineFeed + "-----------------------------------" + lineFeed + fieldComment +
        lineFeed + currentURL;
    }
    document.getElementById("logABugLink1").href=bugLink;
    document.getElementById("logABugLink2").href=bugLink;
    document.getElementById("logABugLink3").href=bugLink;
}
