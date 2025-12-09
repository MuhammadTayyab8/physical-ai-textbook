import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/hackathon-1/__docusaurus/debug',
    component: ComponentCreator('/hackathon-1/__docusaurus/debug', '620'),
    exact: true
  },
  {
    path: '/hackathon-1/__docusaurus/debug/config',
    component: ComponentCreator('/hackathon-1/__docusaurus/debug/config', 'afa'),
    exact: true
  },
  {
    path: '/hackathon-1/__docusaurus/debug/content',
    component: ComponentCreator('/hackathon-1/__docusaurus/debug/content', 'd14'),
    exact: true
  },
  {
    path: '/hackathon-1/__docusaurus/debug/globalData',
    component: ComponentCreator('/hackathon-1/__docusaurus/debug/globalData', '2a1'),
    exact: true
  },
  {
    path: '/hackathon-1/__docusaurus/debug/metadata',
    component: ComponentCreator('/hackathon-1/__docusaurus/debug/metadata', '83a'),
    exact: true
  },
  {
    path: '/hackathon-1/__docusaurus/debug/registry',
    component: ComponentCreator('/hackathon-1/__docusaurus/debug/registry', '779'),
    exact: true
  },
  {
    path: '/hackathon-1/__docusaurus/debug/routes',
    component: ComponentCreator('/hackathon-1/__docusaurus/debug/routes', '377'),
    exact: true
  },
  {
    path: '/hackathon-1/search',
    component: ComponentCreator('/hackathon-1/search', 'd35'),
    exact: true
  },
  {
    path: '/hackathon-1/search',
    component: ComponentCreator('/hackathon-1/search', '0e3'),
    exact: true
  },
  {
    path: '/hackathon-1/docs',
    component: ComponentCreator('/hackathon-1/docs', '4a6'),
    routes: [
      {
        path: '/hackathon-1/docs/foundations',
        component: ComponentCreator('/hackathon-1/docs/foundations', 'ff0'),
        exact: true,
        sidebar: "textbookSidebar"
      },
      {
        path: '/hackathon-1/docs/introduction',
        component: ComponentCreator('/hackathon-1/docs/introduction', '915'),
        exact: true,
        sidebar: "textbookSidebar"
      },
      {
        path: '/hackathon-1/docs/locomotion',
        component: ComponentCreator('/hackathon-1/docs/locomotion', 'f6d'),
        exact: true,
        sidebar: "textbookSidebar"
      }
    ]
  },
  {
    path: '/hackathon-1/',
    component: ComponentCreator('/hackathon-1/', 'b60'),
    exact: true
  },
  {
    path: '/hackathon-1/',
    component: ComponentCreator('/hackathon-1/', 'da2'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
