import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/physical-ai-textbook/__docusaurus/debug',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug', 'fea'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/config',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/config', '317'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/content',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/content', '317'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/globalData',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/globalData', '2ef'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/metadata',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/metadata', '84d'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/registry',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/registry', '032'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/__docusaurus/debug/routes',
    component: ComponentCreator('/physical-ai-textbook/__docusaurus/debug/routes', '2c3'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/search',
    component: ComponentCreator('/physical-ai-textbook/search', '910'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/search',
    component: ComponentCreator('/physical-ai-textbook/search', '4a9'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/docs',
    component: ComponentCreator('/physical-ai-textbook/docs', 'a3b'),
    routes: [
      {
        path: '/physical-ai-textbook/docs/foundations',
        component: ComponentCreator('/physical-ai-textbook/docs/foundations', '5f6'),
        exact: true,
        sidebar: "textbookSidebar"
      },
      {
        path: '/physical-ai-textbook/docs/hri',
        component: ComponentCreator('/physical-ai-textbook/docs/hri', '616'),
        exact: true,
        sidebar: "textbookSidebar"
      },
      {
        path: '/physical-ai-textbook/docs/introduction',
        component: ComponentCreator('/physical-ai-textbook/docs/introduction', '6b1'),
        exact: true,
        sidebar: "textbookSidebar"
      },
      {
        path: '/physical-ai-textbook/docs/locomotion',
        component: ComponentCreator('/physical-ai-textbook/docs/locomotion', '886'),
        exact: true,
        sidebar: "textbookSidebar"
      },
      {
        path: '/physical-ai-textbook/docs/manipulation',
        component: ComponentCreator('/physical-ai-textbook/docs/manipulation', '720'),
        exact: true,
        sidebar: "textbookSidebar"
      }
    ]
  },
  {
    path: '/physical-ai-textbook/',
    component: ComponentCreator('/physical-ai-textbook/', '56c'),
    exact: true
  },
  {
    path: '/physical-ai-textbook/',
    component: ComponentCreator('/physical-ai-textbook/', 'fab'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
