module.exports = {
  title: 'Newcastle Data Analytics',
  description: 'A meetup for all things Data and Analytics.',
  head: [
      ['link', { rel: 'icon', href: `/images/favicon.ico` }]
  ],
  themeConfig: {
      nav: [
        { text: 'Home', link: '/' },
        { text: 'Give a Talk', link: 'https://github.com/newwwie/data-analytics-meetup' },
        { text: 'Meetup', link: 'https://www.meetup.com/Newcastle-data-analytics-meetup/' },
        { text: 'Twitter', link: 'https://twitter.com/NewcastleData' },
        { text: 'Facebook', link: 'https://www.facebook.com/groups/newcastledata' },
        { text: 'Blog', link: '/blog/' },
      ]
  },
  dest: "docs",
  base: "/data-analytics-meetup"
}

