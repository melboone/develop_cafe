Title: How to modify this page
Date: 04 August 2020
Show_date: No
Modified: 11 August 2020
Slug: pages/how-to-modify-this-page
Summary: How to modify Develop Cafe
Github_edit_link: https://github.com/melboone/develop_cafe/edit/master/content/pages/how-to.md

Get started with a [sample file](/theme/extra/page_template.md).

## Format

Every page and article on this website uses Markdown format with `.md` extension. 
Markdown cheat sheet can be found [here](https://www.markdownguide.org/cheat-sheet/).

## Mandatory Elements

Every page, at a minimum, must have the following:

    Title: My super title
    Date: 2010-12-03 10:20
    Slug: category/my-super-title

As you can see the `Slug:` contains the category before the actual slug. This helps 
better categorizing the URLs and avoid confusion.

For general pages, such as this one or [`About`](pages/about.html), category is 
always `pages/`.

A good starting point is the `template_` file created in each category.

## Optional Fields

| **Property** | **Description**                                                                                                                                                                                                                                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Author:      | Set the yourself as the author of the page. You can also include a link to your page with a normal link `Author`.<br>Please don't spam.                                                                                                                                                                                                    |
| <br>Authors: | Multiple authors are supported, example: `Authors: Julian Page, Matthew Smith`.<br>Accepts links for every specific author, example: `Authors: <a href="your_link" rel="noopener noreferrer nofollow">Julian Page</a>, Matthew Smith`.<br>Due to [security](https://www.jitbit.com/alexblog/256-targetblank---the-most-underestimated-vulnerability-ever/) [reasons](https://sites.google.com/site/bughunteruniversity/nonvuln/phishing-with-window-opener) and the high risk of spam, only links with `rel="noopener noreferrer nofollow"` will be accepted. |
| Show_date:   | Display in template the date the article was created.                                                                                                                                                                                                                                                                                      |
| Modified:    | Date of the last modification of the page.                                                                                                                                                                                                                                                                                                 |
| Show_modified: | Display in template the last date the file was modified.                                                                                                                                                                                                                                                                                 |
| Summary:     | Short version for index and feeds                                                                                                                                                                                                                                                                                                          |
| Tags:        | Content tags, separated by commas                                                                                                                                                                                                                                                                                                          |
| keywords:    | Content keywords, separated by commas (HTML content only)                                                                                                                                                                                                                                                                                  |
| category:    | Content category (one only — not multiple)                                                                                                                                                                                                                                                                                                 |
| template:    | Name of template to use to generate content                                                                                                                                                                                                                                                                                                |
| status:      | Content status: `draft`, `hidden`, or `published`                                                                                                                                                                                                                                                                                          |
| translation: | Is content is a translation of another (`true` or `false`)                                                                                                                                                                                                                                                                                 |
| Lang:        | Content language ID (`en`, `fr`, etc.)                                                                                                                                                                                                                                                                                                     |
| Icon:        | Add a link to the SVG icon                                                                                                                                                                                                                                                                                                                 |

## Creating a new page

Create a `.md` file in the appropriate folder (or new one), add the above elements. 
It is a good idea to add the file to 
the [configuration](https://github.com/melboone/develop_cafe/blob/master/pelicanconf.py) 
file as well, in the `MENUITEMS`.

A good starting point is the `template_` file created in each category.

## Private comments

If you want to comment in page but you don't want to show it to the end user, use
`[//]: # (This comment will not be visible to the end user)`