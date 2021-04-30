---
description: Use the following procedure in legacy applications to load a .x file.
ms.assetid: 2b975873-2e5d-4c64-a022-d2098c3d95b8
title: Loading an X File (Legacy) (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Loading an X File (Legacy) (Direct3D 9)

Use the following procedure in legacy applications to load a .x file.

1.  Use the [**DirectXFileCreate**](directxfilecreate.md) function to create an [**IDirectXFile**](idirectxfile.md) object.
2.  If templates are present in the DirectX file that you will load, use the [**IDirectXFile::RegisterTemplates**](idirectxfile--registertemplates.md) method to register those templates.
3.  Use the [**IDirectXFile::CreateEnumObject**](idirectxfile--createenumobject.md) method to create an [**IDirectXFileEnumObject**](idirectxfileenumobject.md) enumerator object.
4.  Loop through the objects in the file. For each object, perform the following steps.
    1.  Use the [**IDirectXFileEnumObject::GetNextDataObject**](idirectxfileenumobject--getnextdataobject.md) method to retrieve each [**IDirectXFileData**](idirectxfiledata.md) object.
    2.  Use the [**IDirectXFileData::GetType**](idirectxfiledata--gettype.md) method to retrieve the data's type.
    3.  Load the data using the [**IDirectXFileData::GetData**](idirectxfiledata--getdata.md) method.
    4.  If the object has optional members, retrieve the optional members by calling the [**IDirectXFileData::GetNextObject**](idirectxfiledata--getnextobject.md) method.
    5.  Release the [**IDirectXFileData**](idirectxfiledata.md) object.
5.  Release the [**IDirectXFileEnumObject**](idirectxfileenumobject.md) object.
6.  Release the [**IDirectXFile**](idirectxfile.md) object.

## Related topics

<dl> <dt>

[X Files (Legacy)](x-files--legacy-.md)
</dt> </dl>

 

 



