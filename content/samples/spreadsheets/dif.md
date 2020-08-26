Title: dif
Slug: samples/spreadsheets/dif-samples
Date: 27 August 2020
Modified: 27 August 2020
Show_modified: Yes
Summary:  DIF (Data Interchange Format) is a text-based file format used for exporting and importing spreadsheets. 
Icon: https://ik.imagekit.io/developcafe/excel-svgrepo-com_ZnvIbjj1a.svg
category: spreadsheets
Github_edit_link: https://github.com/melboone/develop_cafe/edit/master/content/samples/spreadsheets/dif.md

DIF (Data Interchange Format) is a text-based file format used for exporting and importing spreadsheets.

DIF files store data using the ASCII character encoding scheme. This mitigates cross-platform 
issues but at the same time creates certain limitations making the DIF format a more basic one
 when compared to other spreadsheet formats.

DIF files can only handle a single spreadsheet per workbook. DIF spreadsheets are divided 
into two sections, data and header. Header parts start a text identifier written in capital
 letters and data parts start with a number pair indicating the row and column. Cell content 
 is written between quotes.

This are not samples for:

* Raytheon Raster Bitmap
* VisiCalc spreadsheet
* Wright Design's Design Image Format

| File name   | File Size   | Download                            |  Rows   | Columns | File Description                 |
|-------------|-------------|-------------------------------------|---------|---------|----------------------------------|
| DIF-file-1  | 2.0 KB      | [Download](/samples/DIF_file_1.dif) | 11   |   12       | Total text rows: 302.            |
| DIF-file-2  | 17.5 KB     | [Download](/samples/DIF_file_2.dif) | 101  |   12       |                                  |
| DIF-file-3  | 405.7 KB    | [Download](/samples/DIF_file_3.dif) | 1001 |   12       | Total text rows: 79,454          |

