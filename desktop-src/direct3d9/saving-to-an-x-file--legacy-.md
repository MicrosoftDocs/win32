---
description: Use the following procedure in legacy applications to save .x file templates and data to a .x file.
ms.assetid: 5401b381-3599-465a-b41b-e63b7372fc0e
title: Saving to an X File (Legacy) (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Saving to an X File (Legacy) (Direct3D 9)

Use the following procedure in legacy applications to save .x file templates and data to a .x file.

1.  Use the [**DirectXFileCreate**](directxfilecreate.md) function to create an [**IDirectXFile**](idirectxfile.md) object.
2.  Use the [**IDirectXFile::RegisterTemplates**](idirectxfile--registertemplates.md) method to inform the DirectX file system about any templates that you will use.
3.  Use the [**IDirectXFile::CreateSaveObject**](idirectxfile--createsaveobject.md) method to create an [**IDirectXFileSaveObject**](idirectxfilesaveobject.md) object.
4.  Use the [**IDirectXFileSaveObject::SaveTemplates**](idirectxfilesaveobject--savetemplates.md) method to save templates, if desired.
5.  Loop through the objects to save. For each top-level object, perform the following steps.
    -   Use the [**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md) method to create an [**IDirectXFileData**](idirectxfiledata.md) object as a top-level object in the file. If the top-level data object has optional child objects, add them to the object by using the appropriate method from the next step.
    -   Each [**IDirectXFileData**](idirectxfiledata.md) object can have optional child objects if its template allows it. The child objects can be any of the three types of objects: **IDirectXFileData**, [**IDirectXFileDataReference**](idirectxfiledatareference.md), or [**IDirectXFileBinary**](idirectxfilebinary.md). Loop through the objects you need to save, adding each optional child member to the object list in the manner appropriate to its type, as illustrated in the following steps. Then, if the object type is Data, call the [**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md) method to create an **IDirectXFileData** object, and then call the [**IDirectXFileData::AddDataObject**](idirectxfiledata--adddataobject.md) method to add it as a child of the object. If the object type is Data Reference, call the [**IDirectXFileData::AddDataReference**](idirectxfiledata--adddatareference.md) method to create and add the data reference object as a child of the object. Or, if the object type is Binary, call the [**IDirectXFileData::AddBinaryObject**](idirectxfiledata--addbinaryobject.md) method to create and add the binary object as a child of the object.
    -   Call the [**IDirectXFileSaveObject::SaveData**](idirectxfilesaveobject--savedata.md) method to save the data object and its children.
    -   Release the [**IDirectXFileData**](idirectxfiledata.md) object.
6.  Release the [**IDirectXFileSaveObject**](idirectxfilesaveobject.md) object.
7.  Release the [**IDirectXFile**](idirectxfile.md) object.

## Related topics

<dl> <dt>

[X Files (Legacy)](x-files--legacy-.md)
</dt> </dl>

 

 



