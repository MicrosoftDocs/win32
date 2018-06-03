---
title: ITopic interface
description: Help topic interface, contains methods to retrieve topic information
ms.assetid: 02f45f6a-1e5b-4ba1-93a5-2e594f8ef06d
keywords:
- ITopic interface HelpAPI
- ITopic interface HelpAPI , described
topic_type:
- apiref
api_name:
- ITopic
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ITopic interface

Help topic interface, contains methods to retrieve topic information

## Members

The **ITopic** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ITopic** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ITopic** interface has these methods.



| Method                                        | Description                                                                                    |
|:----------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**Category**](itopic-category.md)           | Returns topic categories (if defined in the content)<br/>                                |
| [**ContentFilter**](itopic-contentfilter.md) | Returns the content filter values for the topic<br/>                                     |
| [**ContentType**](itopic-contenttype.md)     | Returns this topic's content types (if defined in the content)<br/>                      |
| [**FetchContent**](itopic-fetchcontent.md)   | method FetchContent - returns a data stream containing the XHTML data for the topic<br/> |



 

### Properties

The **ITopic** interface has these properties.



| Property                                                                           | Access type          | Description                                                                                                                   |
|:-----------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**Catalog**](itopic-catalog.md)<br/>                                       | Read-only<br/> | Returns the catalog interface associated with the topic<br/>                                                            |
| [**Description**](itopic-description.md)<br/>                               | Read-only<br/> | Returns topic description<br/>                                                                                          |
| [**DisplayVersion**](itopic-displayversion.md)<br/>                         | Read-only<br/> | Returns display version<br/>                                                                                            |
| [**Id**](itopic-id.md)<br/>                                                 | Read-only<br/> | Returns topic identifier<br/>                                                                                           |
| [**locale**](itopic-locale.md)<br/>                                         | Read-only<br/> | Returns locale<br/>                                                                                                     |
| [**Package**](itopic-package.md)<br/>                                       | Read-only<br/> | Returns the package that the topic resides in<br/>                                                                      |
| [**ParentId**](itopic-parentid.md)<br/>                                     | Read-only<br/> | Returns topic parent identifier. The value will be -1 if the topic is a root (no parent) topic<br/>                     |
| [**ParentTopicLocale**](itopic-parenttopiclocale.md)<br/>                   | Read-only<br/> | Returns parent topic locale<br/>                                                                                        |
| [**ParentTopicVersion**](itopic-parenttopicversion.md)<br/>                 | Read-only<br/> | Returns parent topic version<br/>                                                                                       |
| [**TableOfContentsHasChildren**](itopic-tableofcontentshaschildren.md)<br/> | Read-only<br/> | For TableOfContents calls, returns true if the topic has children. It will not be relevant data for non-TOC calls.<br/> |
| [**TableOfContentsPosition**](itopic-tableofcontentsposition.md)<br/>       | Read-only<br/> | Returns topics position in the table of contents<br/>                                                                   |
| [**Title**](itopic-title.md)<br/>                                           | Read-only<br/> | Returns topic title<br/>                                                                                                |
| [**TopicLocale**](itopic-topiclocale.md)<br/>                               | Read-only<br/> | Returns topic locale<br/>                                                                                               |
| [**TopicVersion**](itopic-topicversion.md)<br/>                             | Read-only<br/> | Returns topic version<br/>                                                                                              |
| [**Url**](itopic-url.md)<br/>                                               | Read-only<br/> | Returns topic url<br/>                                                                                                  |
| [**Vendor**](itopic-vendor.md)<br/>                                         | Read-only<br/> | Returns the vendor name for the topic<br/>                                                                              |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



 

 





