---
description: This topic describes the structure of an Advanced Systems Format (ASF) file.
ms.assetid: 4a817efa-5452-46bf-8921-2ba199c21949
title: ASF File Structure
ms.topic: article
ms.date: 05/31/2018
---

# ASF File Structure

This topic describes the structure of an Advanced Systems Format (ASF) file.

For detailed information about ASF files, download the [ASF Specification](https://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=56de5ee4-51ca-46c6-903b-97390ad14fea).

The base unit of organization for ASF files is called an *object*. An ASF file object contains the following data.



| Data                                                        | Size     |
|-------------------------------------------------------------|----------|
| A GUID that identifies the object.                          | 128 bits |
| The size of the object.                                     | 64-bits. |
| Object data. The object data can contain other ASF objects. | Varies.  |



 

> [!Note]  
> An ASF file object is simply a chunk of data. It is not an object in the computer programming sense.

 

An ASF file contains three types of top-level file objects.



| ASF File Object                                                                                                                      | Description                                          |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <span id="_Header_Object"></span><span id="_header_object"></span><span id="_HEADER_OBJECT"></span> Header Object<br/>         | Contains information about the ASF file.<br/>  |
| <span id="Data_Object"></span><span id="data_object"></span><span id="DATA_OBJECT"></span>Data Object<br/>                     | Contains packets of media data.<br/>           |
| <span id="_Index_Object_s_"></span><span id="_index_object_s_"></span><span id="_INDEX_OBJECT_S_"></span> Index Object(s)<br/> | Contains one or more indexes. (Optional.)<br/> |



 

The following diagram shows the ASF file structure.

![diagram showing the asf file structure, including items within the header, data, and index](images/asf-components04.png)

This diagram is not drawn to scale; typically the Data Object comprises most of the file.

### Header Object

The Header Object is mandatory and appears at the beginning of every ASF file. It contains global file attributes and information about the streams in the ASF file. This information is used to interpret and play the data in the file.

The Header Object contains several madatory sub-objects:

-   The File Properties Object describes global attributes of the file, such as the file size, play duration, number of data packets, minimum and maximum packet size, and maximum bit rate.
-   The Header Extension Object enables additional functionality to be added to an ASF file while maintaining backward compatibility.
-   The Stream Properties Object describes one stream in the file. An ASF file must contain at least one stream, and therefore at least one Stream Properties Object.

The Header Object can contain additional optional information, including metadata about the file (such as title and author), a list of the codecs used to encode the file, and content protection information.

### Data Object

The ASF Data Object contains all of the media data for the ASF file. This object is mandatory and must follow the ASF Header Object.

The Data Object is divided into data *packets*. Each packet contains data for one or several streams in the file. A data packet contains a data packet header that provides packet parsing information, followed by the payload data the actual digital media data. All of the data packets have a presentation time associated with it and are arranged in the order received.

Information about the contents of the Data Object, such as the packet size and packet count, is stored in the Header Object.

### Index Object

The Index Object is optional and is the last object in the ASF file. An ASF file can contain more than one Index Object. The Index Object provides time-based random access into the ASF Data Object.

A Simple Index Object is another type of index.

## Related topics

<dl> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 




