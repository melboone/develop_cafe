Title: How to modify this page
Date: 04-AUG-2020
Modified: 04-AUG-2020
Slug: how-to-modify-this-page
Summary: How to modify Develop Cafe
Category: FAQ

## Format

Every page and article on this website uses Markdown format with `.md` extension. Markdown basics can be found [here](https://daringfireball.net/projects/markdown/basics).

## - Mandatory Elements

Every page, at a minimum, must have the following:

    Title: My super title
    Date: 2010-12-03 10:20
    Slug: category/my-super-title

    Content

As you can see the `Slug:` has a category before the actual slug. This helps better categorizing the URLs and avoid confusion.
The category is not necessarily for general pages.

For general pages, such as this one or [`About`](/about.html), category is not required.

## Optional Fields

| **Property** | **Description**                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| Author:      | Set the yourself as the author of the page. You can also include a link to your page with a normal link `Author`. Please don't spam. |
| Authors:     | Multiple authors are supported, example: `Author: Julian Page, Matthew Smith`.                                                       |
| Modified:    | Date of the last modification of the page.                                                                                           |
| Summary:     | Short version for index and feeds                                                                                                    |
| Tags:        | Content tags, separated by commas                                                                                                    |
| keywords:    | Content keywords, separated by commas (HTML content only)                                                                            |
| category:    | Content category (one only — not multiple)                                                                                           |
| template:    | Name of template to use to generate content                                                                                          |
| status:      | Content status: `draft`, `hidden`, or `published`                                                                                    |
| translation: | Is content is a translation of another (`true` or `false`)                                                                           |
| lang         | Content language ID (`en`, `fr`, etc.)                                                                                               |

## Creating a new page

To create a new page, create a `.md` file in the appropriate folder (or new one), add the above elements. It is a good idea to add the file to the [configuration](https://github.com/melboone/develop_cafe/blob/master/pelicanconf.py) file as well, in the `MENUITEMS`.
