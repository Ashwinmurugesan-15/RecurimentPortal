// Year filter dropdown injection script
// This script dynamically adds the year filter dropdown to the Monthly Statistics section

(function () {
    'use strict';

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', injectYearFilter);
    } else {
        injectYearFilter();
    }

    function injectYearFilter() {
        // Find the Monthly Statistics card title
        const monthlyStatsCard = document.querySelector('.card.mb-3');
        if (!monthlyStatsCard) return;

        const cardTitle = monthlyStatsCard.querySelector('.card-title');
        if (!cardTitle || !cardTitle.textContent.includes('Monthly Statistics')) return;

        // Get the parent container
        const headerContainer = cardTitle.parentElement;
        if (!headerContainer) return;

        // Check if dropdown already exists
        if (document.getElementById('yearFilter')) return;

        // Create the dropdown
        const dropdown = document.createElement('select');
        dropdown.id = 'yearFilter';
        dropdown.className = 'form-select';
        dropdown.style.cssText = 'width: auto; min-width: 150px; max-width: 200px; font-size: 0.875rem; margin-left: auto;';

        const defaultOption = document.createElement('option');
        defaultOption.value = 'all';
        defaultOption.textContent = 'All Years';
        dropdown.appendChild(defaultOption);

        // Make sure the header container is flex
        headerContainer.style.display = 'flex';
        headerContainer.style.justifyContent = 'space-between';
        headerContainer.style.alignItems = 'center';
        headerContainer.style.padding = '0.5rem 1rem';

        // Add the dropdown
        headerContainer.appendChild(dropdown);

        console.log('✅ Year filter dropdown injected successfully!');
    }
})();
