import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', 'a30'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '9aa'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'ae1'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c93'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '96e'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '062'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '933'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', 'c39'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '7d0'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '356'),
            routes: [
              {
                path: '/docs/foundations',
                component: ComponentCreator('/docs/foundations', '935'),
                exact: true,
                sidebar: "textbookSidebar"
              },
              {
                path: '/docs/introduction',
                component: ComponentCreator('/docs/introduction', '652'),
                exact: true,
                sidebar: "textbookSidebar"
              },
              {
                path: '/docs/locomotion',
                component: ComponentCreator('/docs/locomotion', 'acb'),
                exact: true,
                sidebar: "textbookSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/',
    component: ComponentCreator('/', '6a3'),
    exact: true
  },
  {
    path: '/',
    component: ComponentCreator('/', '2a3'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
