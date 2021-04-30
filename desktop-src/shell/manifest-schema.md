---
description: These elements make up the XML schema used in the Web Publishing and Online Print Ordering wizards' transfer manifest.
title: Transfer Manifest Schema
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 488b6fc9-ff85-4860-9cd5-61d5de7e15e8
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Transfer Manifest Schema

These elements make up the XML schema used in the Web Publishing and Online Print Ordering wizards' transfer manifest.

The following elements are defined for the transfer manifest.

-   [cancelledpage](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [failurepage](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [favorite](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [file](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [filelist](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [folder](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [folderlist](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [formdata](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [htmlui](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [imageproperty](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [metadata](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [netplace](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [post](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [resize](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [successpage](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [target](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [transfermanifest](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)
-   [uploadinfo](#syntax)
    -   [Syntax](#syntax)
    -   [Attributes](#attributes)
    -   [Element Information](#element-information)

## cancelledpage

Specifies the server-side HTML page to display before the wizard is closed when the user clicks the **Cancel** button.

### Syntax


```
<cancelledpage
    href = "string"
>
<!-- child elements -->
</cancelledpage>                  
                    
```



### Attributes



| Attribute | Description                                                                                           |
|-----------|-------------------------------------------------------------------------------------------------------|
| href      | Required. The URL of the server-side HTML page to display when the user clicks the **Cancel** button. |



 

### Element Information



| Parent Element        | Child Elements |
|-----------------------|----------------|
| [uploadinfo](#syntax) | None           |



 

## failurepage

Specifies the server-side HTML page to display if the upload is not successful.

### Syntax


```
<failurepage
    href = "string"
>
<!-- child elements -->
</failurepage>                    
                    
```



### Attributes



| Attribute | Description                                                                                |
|-----------|--------------------------------------------------------------------------------------------|
| href      | Required. The URL of the server-side HTML page to display if the upload is not successful. |



 

### Element Information



| Parent Element        | Child Elements         |
|-----------------------|------------------------|
| [uploadinfo](#syntax) | None. Text is allowed. |



 

## favorite

Instructs the wizard to create a favorite website entry in the **Favorites** menu for the given URL. If this element is not specified, then the [htmlui](#syntax) element is used in its place.

### Syntax


```
<favorite
    comment = "string"
    href = "string"
    name = "string"
>
<!-- child elements -->
</favorite>                   
                    
```



### Attributes



| Attribute | Description                                                            |
|-----------|------------------------------------------------------------------------|
| comment   | Required. The comment associated with the **Favorites** entry.         |
| href      | Required. The URL of the **Favorites** entry.                          |
| name      | Required. The name for the URL that appears in the **Favorites** menu. |



 

### Element Information



| Parent Element        | Child Elements         |
|-----------------------|------------------------|
| [uploadinfo](#syntax) | None. Text is allowed. |



 

## file

Describes a single file to be copied. Multiple [file](#syntax) elements may be contained under a single [filelist](#syntax) node.

### Syntax


```
<file
    contenttype = "string"
    destination = "string"
    extension = "string"
    id = "string"
    size = "string"
    source = "string"
>
<!-- child elements -->
</file>                   
                    
```



### Attributes



| Attribute   | Description                                                                                                                                                                  |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| contenttype | Optional. The MIME type of the file.                                                                                                                                         |
| destination | Required. A suggested path for the file once it is uploaded. This path is relative to the upload site's destination URL. The upload site can modify this value as necessary. |
| extension   | Optional. The file name extension of the file.                                                                                                                               |
| id          | Required. The numerical index of the file.                                                                                                                                   |
| size        | Optional. The size of the file, in bytes.                                                                                                                                    |
| source      | Required. The full file system path for the file.                                                                                                                            |



 

### Element Information



| Parent Element      | Child Elements                                          |
|---------------------|---------------------------------------------------------|
| [filelist](#syntax) | [metadata](#syntax), [post](#syntax), [resize](#syntax) |



 

## filelist

A container for elements describing the files to be copied. Multiple [filelist](#syntax) elements may be contained under a single [transfermanifest](#syntax) node.

### Syntax


```
<filelist
    usesfolders = "1"
>
<!-- child elements -->
</filelist>                   
                    
```



### Attributes



| Attribute   | Description      |
|-------------|------------------|
| usesfolders | Not implemented. |



 

### Element Information



| Parent Element              | Child Elements  |
|-----------------------------|-----------------|
| [transfermanifest](#syntax) | [file](#syntax) |



 

## folder

Describes a folder in which files are stored. Multiple [folder](#syntax) elements may be contained under a single [folderlist](#syntax) node.

### Syntax


```
<folder
    destination = "string"
>
<!-- child elements -->
</folder>                 
                    
```



### Attributes



| Attribute   | Description                                                                                                                                                                    |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| destination | Required. A suggested path for the folder once it is uploaded. This path is relative to the upload site's destination URL. The upload site can modify this value as necessary. |



 

### Element Information



| Parent Element        | Child Elements |
|-----------------------|----------------|
| [folderlist](#syntax) | None           |



 

## folderlist

A container for elements describing the files to be copied. Multiple [folderlist](#syntax) elements may be contained under a single [transfermanifest](#syntax) node.

### Syntax


```
<folderlist>
<!-- child elements -->
</folderlist>                 
                    
```



### Attributes

None.

### Element Information



| Parent Element              | Child Elements    |
|-----------------------------|-------------------|
| [transfermanifest](#syntax) | [folder](#syntax) |



 

## formdata

Describes optional HTML encoded form data that may be transferred with the files. This element is added by the service if it elects to upload the files as a multi-part post. The form data, together with information from the [post](#syntax) element, is used to create the post header.

Multiple [formdata](#syntax) elements may be contained under a single [uploadinfo](#syntax) node.

### Syntax


```
<formdata
    name = "string"
>
<!-- child elements -->
</formdata>                   
                    
```



### Attributes



| Attribute | Description                                                                      |
|-----------|----------------------------------------------------------------------------------|
| name      | Required. Defines the form data name associated with this section of the upload. |



 

### Element Information



| Parent Element        | Child Elements |
|-----------------------|----------------|
| [uploadinfo](#syntax) | None           |



 

## htmlui

The URL of the server-side HTML page to display when the wizard is closed. This element creates a favorite webpage entry in the **Favorites** menu if the [favorite](#syntax) element is absent and the upload site's friendly name is specified.

### Syntax


```
<htmlui
    href = "string"
>
<!-- child elements -->
</htmlui>                 
                    
```



### Attributes



| Attribute | Description                                                                          |
|-----------|--------------------------------------------------------------------------------------|
| href      | Required. The URL of the server-side HTML page to display when the wizard is closed. |



 

### Element Information



| Parent Element        | Child Elements         |
|-----------------------|------------------------|
| [uploadinfo](#syntax) | None. Text is allowed. |



 

## imageproperty

Specifies an image property relating to the file. Multiple [imageproperty](#syntax) elements may be contained under a single [metadata](#syntax) node.

### Syntax


```
<imageproperty
    id = "string"
>
<!-- child elements -->
</imageproperty>                  
                    
```



### Attributes



| Attribute | Description                                  |
|-----------|----------------------------------------------|
| id        | Required. The ID of the particular property. |



 

### Element Information



| Parent Element      | Child Elements         |
|---------------------|------------------------|
| [metadata](#syntax) | None. Text is allowed. |



 

## metadata

A container for elements and text defining metadata for the particular file. Multiple [metadata](#syntax) elements may be contained under a single [file](#syntax) node.

### Syntax


```
<metadata>
<!-- child elements -->
</metadata>                   
                    
```



### Attributes

None.

### Element Information



| Parent Element  | Child Elements           |
|-----------------|--------------------------|
| [file](#syntax) | [imageproperty](#syntax) |



 

## netplace

Defines the target for a network place that is created in **My Network Places** when the upload is complete. Creation of a network place can be prevented through the [**IPublishingWizard::Initialize**](/windows/desktop/api/Shobjidl/nf-shobjidl-ipublishingwizard-initialize) method.

### Syntax


```
<netplace
    comment = "string"
    href = "string"
    name = "string"
>
<!-- child elements -->
</netplace>                   
                    
```



### Attributes



| Attribute | Description                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------|
| comment   | Required. The comment displayed for the network place icon when the cursor rests on it.         |
| href      | Required. The URL of the network place entry.                                                   |
| name      | Required. The name for the network place icon that appears in the **My Network Places** folder. |



 

### Element Information



| Parent Element        | Child Elements         |
|-----------------------|------------------------|
| [uploadinfo](#syntax) | None. Text is allowed. |



 

## post

URL to which the file should be posted. This element is added by the service when the transfer is done as a multi-part post and, with [formdata](#syntax), is used to build the post header. If the service chooses to perform the file transfer using World Wide Web Distributed Authoring and Versioning (WebDAV), it should not add this element. Multiple [post](#syntax) elements may be contained under a single [file](#syntax) node.

### Syntax


```
<post
    filename = "string"
    href = "string"
    name = "string"
>
<!-- child elements -->
</post>                   
                    
```



### Attributes



| Attribute | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| filename  | Optional. The file name for the posted file.                                   |
| href      | Required. The URL of the destination folder.                                   |
| name      | Required. Defines the form data name associated with this section of the post. |



 

### Element Information



| Parent Element  | Child Elements      |
|-----------------|---------------------|
| [file](#syntax) | [formdata](#syntax) |



 

## resize

Defines the scaling and recompression of an image file into JPEG format. If the source file is already in JPEG format and is less than or equal to the specified width and height, it is not sized. If the source file is not a JPEG file, it is converted. Scaling, recompression, and conversion of the file can be prevented through the [**IPublishingWizard::Initialize**](/windows/desktop/api/Shobjidl/nf-shobjidl-ipublishingwizard-initialize) method. Multiple [resize](#syntax) elements may be contained under a single [file](#syntax) node.

### Syntax


```
<resize
    cx = "string"
    cy = "string"
    quality = "string"
>
<!-- child elements -->
</resize>                 
                    
```



### Attributes



| Attribute | Description                                                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cx        | Required. The width of the image, in pixels, after uploading. If this value is 0, then **cx** is calculated from the **cy** value to preserve relative dimensions.  |
| cy        | Required. The height of the image, in pixels, after uploading. If this value is 0, then **cy** is calculated from the **cx** value to preserve relative dimensions. |
| quality   | Required. The JPEG quality value, between 0 and 100, with 100 being the highest quality.                                                                            |



 

### Element Information



| Parent Element  | Child Elements |
|-----------------|----------------|
| [file](#syntax) | None.          |



 

## successpage

Specifies the server-side HTML page to display if the upload is successful.

### Syntax


```
<successpage
    href = "string"
>
<!-- child elements -->
</successpage>                    
                    
```



### Attributes



| Attribute | Description                                                                            |
|-----------|----------------------------------------------------------------------------------------|
| href      | Required. The URL of the server-side HTML page to display if the upload is successful. |



 

### Element Information



| Parent Element        | Child Elements         |
|-----------------------|------------------------|
| [uploadinfo](#syntax) | None. Text is allowed. |



 

## target

A destination folder specified in Universal Naming Convention (UNC) format or as a WebDAV server. The service adds this target to specify a destination folder if the transfer uses a WebDAV or file system protocol. If the service chooses to perform the file transfer as a multi-part post, it should not add this element.

### Syntax


```
<target
    href = "string"
>
<!-- child elements -->
</target>                 
                    
```



### Attributes



| Attribute | Description                                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| href      | Required. The URL of the destination folder. Use the **https://** form for WebDAV or the **\\\\server\\share** form for UNC. |



 

### Element Information



| Parent Element        | Child Elements         |
|-----------------------|------------------------|
| [uploadinfo](#syntax) | None. Text is allowed. |



 

## transfermanifest

The parent node of the transfer manifest file.

### Syntax


```
<transfermanifest>
<!-- child elements -->
</transfermanifest>                   
                    
```



### Attributes

None.

### Element Information



| Parent Element | Child Elements                                                    |
|----------------|-------------------------------------------------------------------|
| None           | [filelist](#syntax), [folderlist](#syntax), [uploadinfo](#syntax) |



 

## uploadinfo

A container for elements providing information from the upload site used in the transaction. Multiple [uploadinfo](#syntax) elements may be contained under a single [transfermanifest](#syntax) node.

### Syntax


```
<uploadinfo
    friendlyname = "string"
>
<!-- child elements -->
</uploadinfo>                 
                    
```



### Attributes



| Attribute    | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| friendlyname | Required. A friendly name for the website which is displayed in the wizard. |



 

### Element Information



| Parent Element              | Child Elements                                                                                                                                           |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [transfermanifest](#syntax) | [cancelledpage](#syntax), [failurepage](#syntax), [favorite](#syntax), [htmlui](#syntax), [netplace](#syntax), [successpage](#syntax), [target](#syntax) |



 

 

 



