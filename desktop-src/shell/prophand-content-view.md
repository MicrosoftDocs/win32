---
description: This topic describes a new view in Windows Explorer, called the Content view, that displays the most relevant content for each item.
title: Content View By File Type or Kind
ms.topic: article
ms.date: 05/31/2018
ms.assetid: E01A6726-14C4-4c00-81D4-AE1008088678
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Content View By File Type or Kind

This topic describes a new view in Windows Explorer, called the Content view, that displays the most relevant content for each item. Using a set of registry keys, items can define a property list and a layout that the Shell uses for Content view. The Shell retrieves the registry keys by using the item's [association array](fa-perceivedtypes.md).

## How Does the Content View Work?

In Windows 7 and later, the Content view uses a resizing logic that drops properties when the window size decreases, to ensure that the most critical properties still have room to be clearly readable. The following screen shot illustrates the Content view of search results containing music, pictures, and documents.

![content view of search results containing music, pictures, and documents](images/content-view/contentviewsearchresults.png)

Some Shell data sources use Content view by default, but users can select the Content view by clicking the **View Control** button in Windows Explorer. A Shell data source extends the Shell namespace and exposes items in a data store. The items in a data store can be indexed by the Windows Search system using a protocol handler.

## How to Implement the Content View

When registering a new [file type](fa-file-types.md) or [protocol handler](../search/-search-3x-wds-extidx-prot-implementing.md), you can take advantage of the Content view by using either of two different approaches. You can use an existing set of properties and layout pattern, or you can create your own combination.

You can use a registry entry to associate your file type or item with a predefined [Kind](../properties/building-property-handlers-user-friendly-kind-names.md), which is a property that you can think of as a content category. By associating your file type or item with certain of these Kinds, you automatically inherit that Kind's Content view layout patterns and property lists. Windows defines Content view layout patterns and property lists for the following Kinds: documents, email, folder, music, picture, and generic. This type of association is encouraged. It lets you provide the consistent experience that a user expects for similar items.

For more information, see [File Types](fa-file-types.md) and [Kind Names](../properties/building-property-handlers-user-friendly-kind-names.md) and [How To Register a Unique Content View Set of Properties and Layout Pattern for the File Type or Item](register-a-unique-content-view-set-of-properties-and-layout-pattern-for-the-file-type-or-item.md).

## Additional Resources

- For property reference documentation, see [System.Kind](../properties/props-system-kind.md), and [System.KindText](../properties/props-system-kindtext.md).
- For PropList reference documentation, see [System.PropList.ContentViewModeForBrowse](../properties/props-system-proplist-contentviewmodeforbrowse.md), and [System.PropList.ContentViewModeForSearch](../properties/props-system-proplist-contentviewmodeforsearch.md).

## Related topics

<dl> <dt>

[Application Registration](app-registration.md)
</dt> <dt>

[File Types](fa-file-types.md)
</dt> <dt>

[How File Associations Work](fa-how-work.md)
</dt> <dt>

[File Type Verifier](file-type-verifier.md)
</dt> <dt>

[File Type Handlers](fa-file-extensions.md)
</dt> <dt>

[Programmatic Identifiers](fa-progids.md)
</dt> <dt>

[Perceived Types](fa-perceivedtypes.md)
</dt> <dt>

[Association Arrays](fa-associationarray.md)
</dt> </dl>

 

 
