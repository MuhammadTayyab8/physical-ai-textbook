// @ts-check
// `@type` JSDoc annotations allow IDEs and type-checking tools to autocomplete

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics Textbook',
  tagline: 'Comprehensive textbook on Physical AI and Humanoid Robotics',
  favicon: 'img/favicon.ico',

  url: 'https://MuhammadTayyab8.github.io',
  baseUrl: '/physical-ai-textbook/',     // <- must match repo name
  organizationName: 'MuhammadTayyab8',
  projectName: 'physical-ai-textbook',   // <- must match repo name

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/MuhammadTayyab8/hackathon-1/edit/main/textbook/',
          routeBasePath: '/docs', // This ensures docs are served from /docs
        },
        blog: false, // Disable blog if not needed
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'Physical AI Textbook',
        // logo: {
        //   alt: 'Physical AI & Humanoid Robotics Logo',
        //   src: 'img/logo.svg',
        // },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'textbookSidebar',
            position: 'left',
            label: 'Textbook Chapters',
          },
          // {
          //   to: '/',
          //   label: 'Home',
          //   position: 'left',
          // },
          {
            href: 'https://github.com/MuhammadTayyab8/hackathon-1',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Content',
            items: [
              {
                label: 'Introduction',
                to: '/docs/introduction',
              },
              {
                label: 'Foundations',
                to: '/docs/foundations',
              },
              {
                label: 'Locomotion',
                to: '/docs/locomotion',
              },
            ],
          },
          {
            title: 'Panaversity',
            items: [
              { label: 'Official Website', href: 'https://panaversity.org' },
              { label: 'AI Native Book', href: 'https://ai-native.panaversity.org' },
            ],
          },
          {
            title: 'Lets Connect',
            items: [
              {
                label: 'linkedin',
                href: 'https://www.linkedin.com/in/muhammad-tayyab-javaid/',
              },
              {
                label: 'Github',
                href: 'https://github.com/MuhammadTayyab8/',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Textbook. Built with Docusaurus.`,
      },
      prism: {
        theme: require('prism-react-renderer').themes.github,
        darkTheme: require('prism-react-renderer').themes.dracula,
      },
    }),
};

module.exports = config;