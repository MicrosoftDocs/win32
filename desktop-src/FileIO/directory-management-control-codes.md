---
Description: Control codes used with file compression and decompression and with reparse points.
ms.assetid: e2e671c7-ef65-4401-8016-649e86f84fec
title: Directory Management Control Codes
ms.topic: article
ms.date: 05/31/2018
---

# Directory Management Control Codes

The following control codes are used with [file compression and decompression](file-compression-and-decompression.md).



| Control Code                                             | Meaning                                                                                                                                     |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**FSCTL\_GET\_COMPRESSION**](https://msdn.microsoft.com/en-us/library/Aa364567(v=VS.85).aspx) | Retrieves the current compression state of a file or directory on a volume whose file system supports per-stream compression.<br/>    |
| [**FSCTL\_SET\_COMPRESSION**](https://msdn.microsoft.com/en-us/library/Aa364592(v=VS.85).aspx) | Sets the compression state of a file or directory on a volume whose file system supports per-file and per-directory compression.<br/> |



 

The following control codes are used with [reparse points](reparse-points.md).

## In this section



| Control Code                                                                   | Description                                                                                                           |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**FSCTL\_DELETE\_REPARSE\_POINT**](https://msdn.microsoft.com/en-us/library/Aa364560(v=VS.85).aspx)<br/> | Deletes a reparse point from the specified file or directory.<br/>                                              |
| [**FSCTL\_GET\_REPARSE\_POINT**](https://msdn.microsoft.com/en-us/library/Aa364571(v=VS.85).aspx)<br/>       | Retrieves the reparse point data associated with the file or directory identified by the specified handle.<br/> |
| [**FSCTL\_SET\_REPARSE\_POINT**](https://msdn.microsoft.com/en-us/library/Aa364595(v=VS.85).aspx)<br/>       | Sets a reparse point on a file or directory.<br/>                                                               |



 

## Related topics

<dl> <dt>

[File Management Control Codes](file-management-control-codes.md)
</dt> <dt>

[Volume Management Control Codes](volume-management-control-codes.md)
</dt> </dl>

 

 




