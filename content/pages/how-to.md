Title: How to modify this page
Date: 04-AUG-2020
Modified: 04-AUG-2020
Slug: how-to-modify-this-page
Summary: How to modify Develop Cafe
Category: FAQ

## Format

Every page and article on this website uses Markdown format. Files have `.md` extension. Markdown basics can be found [here](https://daringfireball.net/projects/markdown/basics).

There are 2 types of pages, stand alone pages, eq. `About` or `Contact` and articles which contain everything else, eq. `Archives` or `zip` sample files.

## Mandatory Elements

Every page or article, at a minimum, must have the following:

    Title: My title
    Date: 2020-12-03 10:20
    Slug: my-title

    Content here

Apart from the above, the articles must be placed in the appropariate category, in the slug field, example: `Slug: archives/zip`.

## Optional Elements

| **Property** | **Description**                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| Author:      | Set the yourself as the author of the page. You can also include a link to your page with a normal link `Author`. Please don't spam. |
| Authors:     | Multiple authors are supported, example: `Author: Julian Page, Matthew Smith`.                                                       |
| Modified:    | Date of the last modification of the page.                                                                                           |
| Summary:     | Short version for index and feeds                                                                                                    |
| Tags:        | Content tags, separated by commas                                                                                                    |
| keywords:    | Content keywords, separated by commas (HTML content only)                                                                            |
| category:    | Content category (one only — not multiple)                                                                                           |
| template     | Name of template to use to generate content                                                                                          |
| status       | Content status: `draft`, `hidden`, or `published`                                                                                    |
| translation  | Is content is a translation of another (`true` or `false`)                                                                           |
| lang         | Content language ID (`en`, `fr`, etc.)                                                                                               |
