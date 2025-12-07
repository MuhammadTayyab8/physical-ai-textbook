import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/hackathon-1/docs',
    component: ComponentCreator('/hackathon-1/docs', 'bbc'),
    routes: [
      {
        path: '/hackathon-1/docs',
        component: ComponentCreator('/hackathon-1/docs', 'cd5'),
        routes: [
          {
            path: '/hackathon-1/docs',
            component: ComponentCreator('/hackathon-1/docs', '627'),
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
          }
        ]
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
