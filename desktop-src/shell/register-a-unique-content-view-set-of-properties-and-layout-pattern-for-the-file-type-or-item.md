---
description: You can register a unique Content view property list and layout pattern for your custom file type or item.
ms.assetid: EA5A3ADA-4DFD-4F85-A176-93577D822815
title: Register a Content View Set of Properties and Layout Pattern for a File Type or Item
ms.topic: how-to
ms.date: 08/18/2026
---

# How to Register a Unique Content View Set of Properties and Layout Pattern for the File Type or Item

You can register a unique Content view property list and layout pattern for your custom file type or item. Register these settings on the ProgID for the file type or item that your application owns. This is the supported way to control which properties Windows displays, and how it arranges them, when the user views your items in Content view.

Register these settings only for the custom file types and ProgIDs that your application owns. Windows determines the Content view for the file types and items that it provides.

Before you register a custom property list for your file type, understand the Search result mode and Browse mode, and the layout patterns that are available to you.

## Instructions

### Step 1: Understanding the Search result mode and Browse mode

Content view requires that you define a layout pattern and a set of property lists for two contexts: an item in a set of search results (Search result mode), and an item that the user browses to in a Shell location (Browse mode). You can use the same values for both modes, or you can define a different property list, a different layout pattern, or both.

Consider how users find your items in each context. When users search for a document-like item, they often search for words in the text of the item. In that case, a layout that includes more sample text produces a more useful search result. The following screenshot shows a Browse content view that includes an excerpt.

![Screenshot that shows a Browse content view that includes a text excerpt.](images/content-view/browsecontentviewkinddocument.png)

When users browse for items, they're rarely looking for particular text. In that case, choose properties and a layout that fit more items on the screen.

### Step 2: Understanding layout patterns

There are four layout patterns: Alpha, Beta, Gamma, and Delta.

**Alpha layout**

The Alpha layout pattern is optimized for document search results that contain excerpts. It has the following specifications:

-   Rows: 4
-   Properties: 7
-   The following illustration shows the Alpha layout when the item has 350 pixels or more of horizontal space.

    ![Diagram that shows the Alpha layout when the item has 350 pixels or more of horizontal space.](images/content-view/layout1.png)

-   The following illustration shows an example of the Alpha layout when the item has 350 pixels or more of horizontal space.

    ![Screenshot that shows an example of the Alpha layout when the item has 350 pixels or more of horizontal space.](images/content-view/alphaviewmore.png)

-   The following illustration shows the Alpha layout when the item has less than 350 pixels of horizontal space.

    ![Diagram that shows the Alpha layout when the item has less than 350 pixels of horizontal space.](images/content-view/layout2.png)

-   The following illustration shows an example of the Alpha layout when the item has less than 350 pixels of horizontal space.

    ![Screenshot that shows an example of the Alpha layout when the item has less than 350 pixels of horizontal space.](images/content-view/alphaviewless.png)

**Beta layout**

The Beta layout pattern is optimized for email search results that contain excerpts. It has the following specifications:

-   Rows: 4
-   Properties: 5
-   The following illustration shows the Beta layout when the item has 350 pixels or more of horizontal space.

    ![Diagram that shows the Beta layout when the item has 350 pixels or more of horizontal space.](images/content-view/layout3.png)

-   The following illustration shows an example of the Beta layout when the item has 350 pixels or more of horizontal space.

    ![Screenshot that shows an example of the Beta layout when the item has 350 pixels or more of horizontal space.](images/content-view/betaviewmore.png)

-   The following illustration shows the Beta layout when the item has less than 350 pixels of horizontal space.

    ![Diagram that shows the Beta layout when the item has less than 350 pixels of horizontal space.](images/content-view/layout4.png)

-   The following illustration shows an example of the Beta layout when the item has less than 350 pixels of horizontal space.

    ![Screenshot that shows an example of the Beta layout when the item has less than 350 pixels of horizontal space.](images/content-view/betaviewless.png)

**Gamma layout**

The Gamma layout pattern is similar to Alpha, but it uses a two-line layout instead of four. This layout is ideal for scenarios in which you want to show a snippet but fit more items on the screen, or for file types that require less space to show the most critical information. The Gamma layout has the following specifications:

-   Rows: 2
-   Properties: 4
-   The following illustration shows the Gamma layout when the item has 350 pixels or more of horizontal space.

    ![Diagram that shows the Gamma layout when the item has 350 pixels or more of horizontal space.](images/content-view/layout5.png)

-   The following illustration shows an example of the Gamma layout when the item has 350 pixels or more of horizontal space.

    ![Screenshot that shows an example of the Gamma layout when the item has 350 pixels or more of horizontal space.](images/content-view/gammaviewmore.png)

-   The following illustration shows the Gamma layout when the item has less than 350 pixels of horizontal space.

    ![Diagram that shows the Gamma layout when the item has less than 350 pixels of horizontal space.](images/content-view/layout6.png)

-   The following illustration shows an example of the Gamma layout when the item has less than 350 pixels of horizontal space.

    ![Screenshot that shows an example of the Gamma layout when the item has less than 350 pixels of horizontal space.](images/content-view/gammaviewless.png)

**Delta layout**

The Delta layout pattern is optimized for displaying many shorter properties, such as the properties of music and picture files. It has the following specifications:

-   Rows: 2
-   Properties: 6
-   The following illustration shows the Delta layout when the item has 700 pixels or more of horizontal space.

    ![Diagram that shows the Delta layout when the item has 700 pixels or more of horizontal space.](images/content-view/layout7.png)

-   The following illustration shows an example of the Delta layout when the item has 700 pixels or more of horizontal space.

    ![Screenshot that shows an example of the Delta layout when the item has 700 pixels or more of horizontal space.](images/content-view/deltalayoutmore.png)

-   The following illustration shows the Delta layout when the item has between 350 and 700 pixels of horizontal space.

    ![Diagram that shows the Delta layout when the item has between 350 and 700 pixels of horizontal space.](images/content-view/layout8.png)

-   The following illustration shows an example of the Delta layout when the item has between 350 and 700 pixels of horizontal space.

    ![Screenshot that shows an example of the Delta layout when the item has between 350 and 700 pixels of horizontal space.](images/content-view/deltaviewbetween.png)

-   The following illustration shows the Delta layout when the item has less than 350 pixels of horizontal space.

    ![Diagram that shows the Delta layout when the item has less than 350 pixels of horizontal space.](images/content-view/layout9.png)

-   The following illustration shows an example of the Delta layout when the item has less than 350 pixels of horizontal space.

    ![Screenshot that shows an example of the Delta layout when the item has less than 350 pixels of horizontal space.](images/content-view/deltaviewless.png)

### Step 3: Registering custom properties and a layout for your file type

After you understand the Search result mode, the Browse mode, and the layout patterns, you can register a custom property list for your file type.

**To register a custom property list and layout pattern for your file type**

1.  Choose from the four layout patterns: Alpha, Beta, Gamma, or Delta.
2.  Consider the following formatting rules, which apply equally to all four layout patterns:
    -   Property 1 always appears in a larger font size. The large font size is usually used for the item name, but you can also use it for the anchor or another item property.
    -   Property 4 is intended for excerpts in the Alpha, Beta, and Gamma layout patterns. This property is allotted more space in those patterns, and it appears in a gray font color rather than black, to help it stand out.
    -   The pixel measurements in this article are relative pixels. The size includes the icon or thumbnail to the left of the properties, and the space between the icon or thumbnail and the selection rectangle.
    -   Most properties have a minimum display size, so they don't appear if there isn't enough space for them at a particular view size. The minimum size is usually 100 pixels wide.
    -   Each layout pattern defines the number of rows and the number of properties in each row.
3.  Decide which properties you want to display in the layout, and where you want to display each property. When you decide which property to display in each position in the layout, consider the typical length of the property, its importance to the user, and whether it should be dropped when the window is too small to contain all of the properties.
4.  Register a layout pattern and a property list for your file type or item type by adding the following values under the ProgID registry key for the file type or item. The following example uses the `Contoso.xyzfile` ProgID for the .xyz file type.

    ```
    HKEY_CLASSES_ROOT
       Contoso.xyzfile
          (ContentViewModeForBrowse) = <PropertyList>
          (ContentViewModeForSearch) = <PropertyList>
          (ContentViewModeLayoutPatternForBrowse) = <Layout pattern name (alpha, beta, delta, or gamma)>
          (ContentViewModeLayoutPatternForSearch) = <Layout pattern name (alpha, beta, delta, or gamma)>
    ```

5.  Observe the following formatting guidelines when you register properties:

    -   Each registration starts with `prop:`.
    -   Each property requires the full property name.
    -   Separate properties with a semicolon and no space.
    -   Properties appear in the order that the selected layout pattern defines.
    -   `~` indicates that the property label isn't displayed.
    -   Use `~System.LayoutPattern.PlaceHolder` if you want to leave blank a property that the layout pattern specifies.
    -   List a property for each position that the layout pattern defines. The Alpha pattern defines seven properties, so the following example lists seven. If you list fewer properties than the pattern defines, the remaining positions stay empty.

    The following sample registry key illustrates these formatting guidelines.

    ```
    HKEY_CLASSES_ROOT
       Contoso.xyzfile
          (ContentViewModeForBrowse) = prop:~System.ItemNameDisplay;System.Author;~System.LayoutPattern.PlaceHolder;System.Keywords;System.DateModified;~System.Size;System.ItemTypeText
          (ContentViewModeLayoutPatternForBrowse) = alpha
    ```

## Related topics

- [File Types](fa-file-types.md)
- [System.LayoutPattern.ContentViewModeForBrowse](../properties/props-system-layoutpattern-contentviewmodeforbrowse.md)
- [System.LayoutPattern.ContentViewModeForSearch](../properties/props-system-layoutpattern-contentviewmodeforsearch.md)
- [System.PropList.ContentViewModeForBrowse](../properties/props-system-proplist-contentviewmodeforbrowse.md)
- [System.PropList.ContentViewModeForSearch](../properties/props-system-proplist-contentviewmodeforsearch.md)
