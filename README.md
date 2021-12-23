# Wiki

![CS50 Web Programming - Wiki](https://user-images.githubusercontent.com/83538534/147208298-f5cddfc0-0418-4631-a951-bbaacbf629c4.gif)

### A Wikipedia-like online encyclopedia

The application uses Markdown to represent each encyclopedia entry. When the user visits a page, it it converted from Markdown into HTML before it is displayed to the user.

- **Entry Page:** Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.

- **Index Page:** The user can click on any entry name to be taken directly to that entry page.

- **Search:** Allows the user to type a query into the search box in the sidebar to **search** for an encyclopedia entry.

- **New Page:** Clicking Create New Page in the sidebar takes the user to a page where they can create a new encyclopedia entry.

- **Edit Page:** On each entry page, the user is able to click a link to be taken to a page where **the user can edit that entry**’s Markdown content in a textarea.

- **Random Page:** Clicking Random Page in the sidebar should take user to a random encyclopedia entry.

- **Markdown to HTML Conversion:** On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user. You may use the python-markdown2 package to perform this conversion, installable via `pip3 install markdown2`.
