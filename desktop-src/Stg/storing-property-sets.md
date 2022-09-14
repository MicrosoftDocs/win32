---
title: Storing Property Sets
description: Applications can expose some of the state data of their documents so that other applications can locate and read that data.
ms.assetid: 2e0b5f6c-da1d-47f2-a50d-1ac7f2f0c45d
keywords:
- Storing Property Sets Structured Storage
ms.topic: article
ms.date: 05/31/2018
---

# Storing Property Sets

Applications can expose some of the state data of their documents so that other applications can locate and read that data. Some examples are a property set describing the author, title, and keywords of a document created with a word processor, or the list of fonts used in a document. This facility is not restricted to documents; it can also be used on embedded objects. Generally, access to property sets should be through the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) and [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interfaces, but this section describes the previously recommended way.

> [!Note]  
> If storing a property set that is internal to your application, you may not want to use the following guidelines. To expose your property set to other applications, follow these guidelines.

 

**To store a property set in a compound file**

1.  Create an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) or [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) instance in the same level of the storage structure as its data streams. Follow the name of your **IStorage** or **IStream** instance with "\\005." Stream and storage names that begin with 0x05 are reserved for common property sets that can be shared among applications. Also, streams beginning with that value are limited to 256 KB. The names can be selected from either published names and formats, or by assigning the property set a FMTID and deriving the name from the FMTID according to the conventions described in [Storage Object Naming Conventions](storage-object-naming-conventions.md).
2.  A property set may be stored in a single [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) instance or in an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) instance containing multiple streams and storages. In the case of an **IStorage** instance, the contained stream named Contents is the primary stream containing property values, where some values may be names of other streams or storage instances within the storage for this property set.
3.  Specify the CLSID of the object class that can display or provide programmatic access to the property values. If there is no such class, the CLSID should be set to the format identifier of the property set. For a property set that uses an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) instance, either set the CLSID of the **IStorage** instance to be the same as that stored in the Contents stream or to **CLSID\_NULL**; the value in a newly created **IStorage** instance.
4.  You have the option of specifying displayable names that form the contents of the dictionary.

Some applications can read only implementations of property sets stored as [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) instances. Applications should be written to expect that a property set may be stored in either an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) or **IStream** instance, unless the property set definition indicates otherwise. For example, the Summary Information property set definition states that it can only be stored in a named **IStream** instance. In cases where you are searching for a property set and do not know whether it is a storage or stream, look for an **IStream** instance with your property set name first. If that fails, look for an **IStorage** instance.

To better understand storing property sets in an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) implementation, suppose there is a class of applications that edit information about animals. First, a CLSID (CLSID\_AnimalApp) is defined for this set of applications, so they can indicate that they understand property sets that contain animal information (**FMTID\_AnimalInfo**), and others that contain medical information (**FMTID\_MedicalInfo**).

``` syntax
IStorage (File): "C:\OLE\REVO.DOC" 
  IStorage: "\005AnimalInfo", CLSID = CLSID_AnimalApp 
    IStream: "Contents" 
      WORD wByteOrder, WORD wFmtVersion, DWORD dwOSVer, 
      CLSID CLSID_AnimalApp, DWORD cSections... 
      ... 
      FMTID = FMTID_AnimalInfo 
      Property: Type = PID_ANIMALTYPE, Type = VT_LPWSTR, 
              Value = L"Dog" 
      Property: Type = PID_ANIMALNAME, Type = VT_LPWSTR, 
              Value = L"Revo" 
      Property: Type = PID_MEDICALHISTORY, Type = VT_STREAMED_OBJECT, 
              Value = "MedicalInfo" 
      ... 
    IStream: "MedicalInfo" 
      WORD wByteOrder, WORD wFmtVersion, DWORD dwOSVer, 
      CLSID CLSID_AnimalApp, DWORD cSections... 
      ... 
      FMTID = CLSID_MedicalInfo 
      Property: Type = PID_VETNAME, Type = VT_LPWSTR, 
              Value = L"Dr. Woof" 
      Property: Type = PID_LASTEXAM, Type = VT_DATE, Value = ...
```

Be aware that the CLSID of the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface and both property sets is **CLSID\_AnimalApp**. This identifies any application that can display and/or provide programmatic access to these property sets. Any application can read the data within the property sets (the point behind property sets), but only applications identified with the class identifier of CLSID\_AnimalApp can understand the meaning of the data in the property sets.

 

 




