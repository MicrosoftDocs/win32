---
title: File Monikers
description: File Monikers
ms.assetid: 923f798d-d789-4e6d-b27e-dd5a72f92abf
ms.topic: article
ms.date: 05/31/2018
---

# File Monikers

*File monikers* are the simplest moniker class. File monikers can be used to identify any object that is stored in its own file. A file moniker acts as a wrapper for the path name the native file system assigns to the file. Calling [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject) for this moniker would cause this object to be activated and then would return an interface pointer to the object. The source of the object named by the moniker must provide an implementation of the [**IPersistFile**](/windows/desktop/api/ObjIdl/nn-objidl-ipersistfile) interface to support binding a file moniker. File monikers can represent either a complete or a relative path.

For example, the file moniker for a spreadsheet object stored as the file C:\\Work\\MySheet.xls would contain information equivalent to that path name. The moniker would not necessarily consist of the same string, however. The string is just its *displayÂ name*, a representation of the moniker's contents that is meaningful to an end user. The display name, which is available through the [**IMoniker::GetDisplayName**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-getdisplayname) method, is used only when displaying a moniker to an end user. This method gets the display name for any of the moniker classes. Internally, the moniker may store the same information in a format that is more efficient for performing moniker operations but isn't meaningful to users. Then, when this same object is bound through a call to the [**BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject) method, the object would be activated, probably by loading the file into the spreadsheet.

OLE offers moniker providers the helper function [**CreateFileMoniker**](/windows/desktop/api/Objbase/nf-objbase-createfilemoniker) that creates a file moniker object and returns its pointer to the provider.

## Related topics

<dl> <dt>

[Anti-Monikers](anti-monikers.md)
</dt> <dt>

[Class Monikers](class-monikers.md)
</dt> <dt>

[Composite Monikers](composite-monikers.md)
</dt> <dt>

[Item Monikers](item-monikers.md)
</dt> <dt>

[Pointer Monikers](pointer-monikers.md)
</dt> </dl>

 

 




