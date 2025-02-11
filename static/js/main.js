// Initialize Calendly widget
function initCalendly() {
    Calendly.initInlineWidget({
        url: 'https://calendly.com/ecomback',
        parentElement: document.querySelector('.calendly-inline-widget'),
        prefill: {},
        utm: {}
    });
}

// Generate accessibility statement
function generateStatement() {
    window.location.href = '/generate-statement';
}

// FAQ accordion functionality
document.addEventListener('DOMContentLoaded', function() {
    const faqItems = document.querySelectorAll('.faq-item h3');
    
    faqItems.forEach(item => {
        item.addEventListener('click', () => {
            const content = item.nextElementSibling;
            content.style.display = content.style.display === 'none' ? 'block' : 'none';
        });
    });

    // Initialize Calendly
    initCalendly();

    // Handle video placeholder click
    document.querySelector('.video-placeholder')?.addEventListener('click', function() {
        const videoContainer = this.parentElement;
        const videoEmbed = document.createElement('iframe');
        videoEmbed.src = 'https://www.youtube-nocookie.com/embed/your-video-id';
        videoEmbed.width = '100%';
        videoEmbed.height = '100%';
        videoEmbed.frameBorder = '0';
        videoEmbed.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
        videoEmbed.allowFullscreen = true;

        videoContainer.innerHTML = '';
        videoContainer.appendChild(videoEmbed);
    });
});