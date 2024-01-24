---
description: You can register a unique Content view property list and layout pattern for the file type or item.
ms.assetid: EA5A3ADA-4DFD-4F85-A176-93577D822815
title: Register a Content View Set of Properties and Layout Pattern for a File Type or Item
ms.topic: article
ms.date: 05/31/2018
---

# How to Register a Unique Content View Set of Properties and Layout Pattern for the File Type or Item

You can register a unique Content view property list and layout pattern for the file type or item. If your file type or item is also associated with a Kind, the specific Content view registration of the file type or item will override the Kind registration. This might be useful if the most important properties for this item are different from other items of the same Kind. If you do not associate your file type or item with an item Kind or directly register the Content view, the system uses the default Content view information (stored in a registry key referenced by the last element in all items' association array, HKEY\_CLASSES\_ROOT\\\*)

Before registering a custom property list for your file type, you should understand the Search Result mode and Browse mode, and the layout patterns that are available to you.

## Instructions

### Step 1: Understanding the Search Result Mode and Browse Mode

Content view requires defining a layout pattern and set of property lists for an item in a set of search results (Search result mode), and when browsing to a Shell location (Browse mode). You can use the same values for Search result and Browse, as `Kind.Music` does. Alternatively, you can define a different property list and/or layout pattern as `Kind.Document` does.

In the case of `Kind.Document`, users often search for words in the text of the document. Therefore, including more sample text in the search result might be the best choice. The following example illustrates the Browse Content view of `Kind.Document`.

![browse content view of kind.document](images/content-view/browsecontentviewkinddocument.png)

Because users are rarely looking for particular text when browsing for documents, optimizing your choice of properties and layout to fit more search results on the screen might be the best choice. The following screen shot illustrates the Search Content view of `Kind.Document`.

### Step 2: Understanding Layout Patterns

There are four layout patterns: Alpha, Beta, Gamma, and Delta.

**Alpha layout**

The Alpha layout pattern is optimized for document search results that contain excerpts. It has the following specifications:

-   Rows: 4
-   Properties: 7
-   Alpha layout when the item has 350 pixels or more of horizontal space, as shown in the following illustration.

    ![alpha layout pattern](images/content-view/layout1.png)

-   The following illustration shows the Alpha layout when the item has 350 pixels or more of horizontal space.

    ![Diagram that shows an alpha layout example](images/content-view/alphaviewmore.png)

-   The following illustration shows the Alpha layout when the item has less than 350 pixels of horizontal space.

    ![Screenshot that shows an alpha layout example in Microsoft Word.](images/content-view/layout2.png)

-   The following illustration shows the Alpha layout when the item has less than 350 pixels of horizontal space.

    ![alpha layout example](images/content-view/alphaviewless.png)

**Beta Layout**

The Beta layout pattern is optimized for email document search results that contain excerpts. It has the following specifications:

-   Rows: 4
-   Properties: 5
-   Beta layout when the item has 350 pixels or more of horizontal space, as shown in the following illustration.

    ![Diagram that shows a beta layout example.](images/content-view/layout3.png)

-   The following illustration shows the beta layout when the item has 350 pixels or more of horizontal space.

    ![Screenshot that shows a beta layout example for e-mail.](images/content-view/betaviewmore.png)

-   The following illustration shows the Beta layout when the item has less than 350 pixels of horizontal space.

    ![Diagram that shows a beta layout example with less than 350 pixels of horizontal space.](images/content-view/layout4.png)

-   The following illustration shows the beta layout when the item has less than 350 pixels of horizontal space:

    ![beta layout example](images/content-view/betaviewless.png)

**Gamma Layout**

The Gamma layout pattern is similar to Alpha but uses a two-line layout instead of four. This layout is ideal for scenarios in which you want to see a snippet but want to fit more items on the screen, or for file types that require less space to show the most critical information. The Gamma layout has the following specifications:

-   Rows: 2
-   Properties: 4
-   The following illustration shows the gamma layout when the item has 350 pixels or more of horizontal space.

    ![Diagram that shows a gamma layout example.](images/content-view/layout5.png)

-   The following illustration shows the gamma layout when the item has 350 pixels or more of horizontal space.

    ![Screenshot that shows a gamma layout example for a checklist item.](images/content-view/gammaviewmore.png)

-   The following illustration shows the gamma layout when the item has less than 350 pixels of horizontal space.

    ![Diagram that shows a gamma layout example with less than 350 pixels of horizontal space.](images/content-view/layout6.png)

-   Example of the gamma layout when the item has less than 350 pixels of horizontal space.

    ![gamma layout example](images/content-view/gammaviewless.png)

**Delta Layout**

The Delta layout pattern is optimized for displaying many shorter properties such as for music and pictures. It has the following specifications:

-   Rows: 2
-   Properties: 6
-   Delta layout when the item has 700 pixels or more of horizontal space, as shown in the following illustration.

    ![Diagram that shows a delta layout example.](images/content-view/layout7.png)

-   Example of the delta layout when the item has 700 pixels or more of horizontal space.

    ![Screenshot that shows a delta layout example for a music file.](images/content-view/deltalayoutmore.png)

-   Delta layout when the item has between 350 and 700 pixels of horizontal space.

    ![Diagram that shows a delta layout example that has between 350 and 700 pixels of horizontal space.](images/content-view/layout8.png)

-   Example of the delta layout when the item has between 350 and 700 pixels of horizontal space.

    ![delta layout example](images/content-view/deltaviewbetween.png)

-   Delta layout when the item has less than 350 pixels of horizontal space.

    ![layout example](images/content-view/layout9.png)

-   Example of the delta layout when the item has less than 350 pixels of horizontal space.

    ![Screenshot that shows a delta layout example for a music file that has less than 350 pixels of horizontal space.](images/content-view/deltaviewless.png)

### Step 3: Registering Custom Properties and Layout for Your File Type

After you understand the Search Result mode, the Browse mode, and the layout patterns, you can register a custom property list for your file type.

**To register a custom property list and layout pattern for your file type.**

1.  Choose from the four layout patterns: Alpha, Beta, Gamma, or Delta.
2.  Consider the following formatting rules, which apply equally to all four layout patterns:
    -   Property 1 is always displayed in a larger font size. The large font size usually used for the item name, but can also be used for the anchor or other item property.
    -   Property 4 is intended for excerpts in the Alpha, Beta, and Gamma layout patterns. This property is allotted more space in those patterns and is displayed in a gray font color, as opposed to black like the other properties, to help it stand out.
    -   The pixel measurements below are in relative pixels, and the size includes the icon/thumbnail to the left of the properties and the space between the icon/thumbnail and the selection rectangle.
    -   Most properties have a minimum display size. Therefore, they will not appear if there is not enough space for them at a particular view size. The minimum size is usually 100 pixels wide.
    -   Each layout pattern defines the number of rows and the number of properties in each row.
3.  Decide which properties you want to display in the layout, and which property you want to display in each location. When deciding which property to display in each position in the layout, consider the typical length of the property, its importance to the user, and whether it should be dropped when the window size is too small to contain all properties.
4.  Register a layout pattern and a property list for your file type or item type by adding the following keys under the ProgID registry key for the file type or item (in this example, for the .xyz file type).

    ```
    HKEY_CLASSES_ROOT\*
       Contoso.xyzfile
          (ContentViewModeForBrowse) = <Layout pattern name (Alpha, Beta, Delta, or Gamma)>
          (ContentViewModeForSearch) = <Layout pattern name (Alpha, Beta, Delta, or Gamma)>
          (ContentViewModeLayoutPatternForBrowse) = <PropertyList>
          (ContentViewModeLayoutPatternForSearch) = <PropertyList>
    ```

5.  Observe the following formatting guidelines for registering properties:

    -   Each registration starts with `prop:`
    -   Each property requires the full property name.
    -   Properties are separated by a semicolon with no space.
    -   Properties are displayed in the order defined by the selected layout pattern.
    -   `~` indicates that the property label should not be displayed.
    -   `~System.LayoutPattern.PlaceHolder` should be used if you want to leave blank a property that is specified in the layout pattern.

    The following sample registry key illustrates these formatting guidelines.

    ```
    HKEY_CLASSES_ROOT\
       Kind.Document
          (ContentViewModeForBrowse) = <PropertyList>
    ```

    Possible values for (ContentViewModeForBrowse) include the following: prop:~System.ItemNameDisplay;System.Author;System.LayoutPattern.Placeholder;System.Keywords;System.DateModified; ~System.Size

## Remarks

## Related topics

<dl> <dt>

[File Types](fa-file-types.md)
</dt> <dt>

[Kind Names](../properties/building-property-handlers-user-friendly-kind-names.md)
</dt> <dt>

[System.PropList.ContentViewModeForBrowse](../properties/props-system-proplist-contentviewmodeforbrowse.md)
</dt> <dt>

[System.PropList.ContentViewModeForSearch](../properties/props-system-proplist-contentviewmodeforsearch.md)
</dt> </dl>

 

 
