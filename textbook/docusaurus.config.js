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
            'https://github.com/MuhammadTayyab8/physical-ai-textbook/edit/main/textbook/',
          routeBasePath: '/docs', // This ensures docs are served from /docs
          showLastUpdateTime: true,
          editCurrentVersion: true,
        },
        blog: false, // Disable blog if not needed
        theme: {
          customCss: './src/css/custom.css',
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
        },
      }),
    ],
  ],

  plugins: [
    // Additional plugins can be added here
  ],

  clientModules: [
    require.resolve('./src/utils/environment.js'),
  ],

  themes: [
    [
      "@easyops-cn/docusaurus-search-local",
      {
        hashed: true,
        language: ["en"],
        docsRouteBasePath: "/docs",
        indexDocs: true,
        indexBlog: false,  // Disable blog indexing
        indexPages: false, // Disable page indexing - this might prevent the error
        ignoreFiles: [     // Exclude files that might be causing parsing issues
          "manipulation.md",
          "hri.md"
        ],
      },
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
          // src: 'img/logo.svg',
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
            href: 'https://github.com/MuhammadTayyab8/physical-ai-textbook',
            label: 'GitHub',
            position: 'right',
          },
          {
            type: 'search', // Add search bar to navbar
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
              {
                label: 'Manipulation',
                to: '/docs/manipulation',
              },
              {
                label: 'Human-Robot Interaction',
                to: '/docs/hri',
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
        theme: require('prism-react-renderer/themes/github'),
        darkTheme: require('prism-react-renderer/themes/dracula'),
      },
    }),
};

module.exports = config;