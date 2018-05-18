---
title: Class Monikers
description: Although classes are typically identified directly with CLSIDs to functions such as CoCreateInstance or CoGetClassObject, classes may also now be identified with a moniker called a class moniker.
ms.assetid: '63f5d256-cb61-4673-b5d6-da5c1d89dfa5'
---

# Class Monikers

Although classes are typically identified directly with CLSIDs to functions such as [**CoCreateInstance**](cocreateinstance.md) or [**CoGetClassObject**](cogetclassobject.md), classes may also now be identified with a moniker called a *class moniker*. Class monikers bind to the class object of the class for which they are created.

The ability to identify classes with a moniker supports useful operations that are otherwise unwieldy. For example, file monikers traditionally supported rich binding only to the class associated with the class of file they referred to; a moniker to an Excel file would bind to an instance of an Excel object, and a moniker to a GIF image would bind to an instance of the currently registered GIF handler. A class moniker allows you to indicate the class you want to use to manipulate a file through composition with a file moniker. A class moniker for a 3D charting class composed with a moniker to an Excel file yields a moniker that binds to an instance of the 3D charting object and initializes the object with the contents of the Excel file.

Class monikers are therefore most useful in composition with other types of monikers, such as file monikers or item monikers.

Class monikers may also be composed to the right of monikers supporting binding to the [**IClassActivator**](iclassactivator.md) interface. When composed in this manner, **IClassActivator** simply gives access to the class object and instances of the class through [**IClassActivator::GetClassObject**](iclassactivator-getclassobject.md). Class monikers may be identified through [**IMoniker::IsSystemMoniker**](imoniker-issystemmoniker.md), which returns MKSYS\_CLASSMONIKER in *pdwMksys*.

Programmers typically create class monikers using the [**CreateClassMoniker**](createclassmoniker.md) function or through [**MkParseDisplayName**](mkparsedisplayname.md). (See [**IMoniker::ParseDisplayName**](imoniker-parsedisplayname.md) for details.)

## Related topics

<dl> <dt>

[Anti-Monikers](anti-monikers.md)
</dt> <dt>

[Composite Monikers](composite-monikers.md)
</dt> <dt>

[File Monikers](file-monikers.md)
</dt> <dt>

[Item Monikers](item-monikers.md)
</dt> <dt>

[Pointer Monikers](pointer-monikers.md)
</dt> </dl>

 

 




