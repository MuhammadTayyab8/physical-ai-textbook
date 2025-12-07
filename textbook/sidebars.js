// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  textbookSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'introduction',
      ],
      link: {
        type: 'doc',
        id: 'introduction',
      },
    },
    {
      type: 'category',
      label: 'Fundamentals',
      items: [
        'foundations',
      ],
    },
    {
      type: 'category',
      label: 'Systems and Applications',
      items: [
        'locomotion',
      ],
    },
  ],
};

module.exports = sidebars;