module.exports = {
  title: 'Hunter Data Analytics Meetup',
  description: 'A meetup for all things Data and Analytics.',
  head: [
      ['link', { rel: 'icon', href: `/images/favicon.ico` }]
  ],
  themeConfig: {
      nav: [
        { text: 'Home', link: '/' },
        { text: 'Give a Talk', link: 'https://github.com/newwwie/data-analytics-meetup' },
        { text: 'Meetup', link: 'https://www.meetup.com/hunter-data-analytics/' },
        { text: 'Twitter', link: 'https://twitter.com/HunterAnalytics' },
        { text: 'Facebook', link: 'https://www.facebook.com/hunteranalytics' },
        { text: 'Blog', link: '/blog/' },
      ]
  },
  dest: "docs",
  base: "/data-analytics-meetup"
}

