---
description: The Microsoft Windows Journal Note Reader component provides programmatic read access to files in the Journal format.
ms.assetid: 85dcda59-2972-48e3-a9f5-5cce0b60a1f1
title: Using the Journal Reader Component
ms.topic: article
ms.date: 05/31/2018
---

# Using the Journal Reader Component

The Microsoft Windows Journal Note Reader component provides programmatic read access to files in the Journal format.

## Component Overview

Journal files have the .jnt file extension. This simple component takes a stream containing a .jnt file and returns a stream containing the file's content in XML format. The XML returned by the component conforms to the Journal Note Reader schema. This schema is documented in [Journal Reader Schema Reference](journal-reader-schema-reference.md).

The component does not provide the ability to write out .jnt files.

The component is available in unmanaged and managed versions. The unmanaged component is available in the journal.dll dynamic link library (DLL). The managed version is either in the Microsoft.Ink.Journal.dll assembly (for redistribution to Windows XP Tablet PC Edition or Windows Vista), or Microsoft.Ink.dll.

> [!IMPORTANT]
>
> Beginning with Windows 10, version 1607, journal.dll is not included in the Windows operating system. That library should be considered deprecated or obsolete and should not be used.

 

### Assembly Changes of Note

It is important to be aware of some changes to the assembly containing the Journal Note Reader component that occurred between the version released in conjunction with version 1.7 of the Tablet Developers Kit and the version that ships in the Windows Vista operating system.

The 1.7 version of the reader component, which can be redistributed to either Windows XP or Windows Vista, is contained in an assembly called Microsoft.Ink.Journal.dll. The reader component ships in Windows Vista, but has been integrated into the core Microsoft.Ink.dll assembly. This means that applications that make use of the 1.7 assembly need to redistribute that assembly with their setup.

## Using the Component

The Journal Note Reader component is useful for extracting the ink data and other information about the file from a Journal file.

### COM

The Journal Note Reader COM component is in the file Journal.dll, which is installed and registered when you download and run the Journal Note Reader installation file.

The COM component does not support the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface.

### Managed

The Journal Note Reader managed component is in the Microsoft.Ink.JournalReader.dll assembly. This assembly is installed and registered in the global assembly cache when you run the Journal Note Reader installation file.

Add a reference to the assembly to use it in your managed project.

## Related topics

<dl> <dt>

[**IJournalReader Interface**](ijournalreader.md)
</dt> <dt>

[Journal Reader Schema Reference](journal-reader-schema-reference.md)
</dt> </dl>

 

 
