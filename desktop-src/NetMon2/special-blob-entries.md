---
description: The following examples use the SetStringInBlob function to create special BLOB entries.
ms.assetid: 4a921b0d-9934-48e2-8837-be0bd7b7fa7a
title: Special BLOB Entries
ms.topic: article
ms.date: 05/31/2018
---

# Special BLOB Entries

The following examples use the [**SetStringInBlob**](setstringinblob.md) function to create special BLOB entries.

## NPP Name

``` syntax
SetStringInBlob(
   hBlob,
   OWNER_NPP,
   CATEGORY_LOCATION,
   TAG_NAME,
   "My NPP Name"); 
```

## NPP Class Identifier

``` syntax
SetClassIDInBlob(
   hBlob,
   OWNER_NPP,
   CATEGORY_LOCATION,
   TAG_CLASSID,
   &CLSID_ThisNPP);
```

## CFGPROC Procedure Name

``` syntax
SetStringInBlob(
   hBlob,
   OWNER_NPP,
   CATEGORY_FINDER,
   TAG_PROCNAME,
   "MyGetNPPBlobs");
```

## Tree Root Name for Finder UI

``` syntax
SetStringInBlob(
   hBlob,
   OWNER_NPP,
   CATEGORY_FINDER,
   TAG_ROOT,
   "My Tree Root name");
```

## Display String for Finder UI

``` syntax
SetStringInBlob(
   hBlob,
   OWNER_NPP,
   CATEGORY_FINDER,
   TAG_DISP_STRING,
   "Double click to select my UI");
```

## Interface Tags

This example includes every interface supported by the NPP.

``` syntax
SetBoolInBlob(  
   hBlob,
   OWNER_NPP,
   CATEGORY_CONFIG,
   TAG_INTERFACE_REALTIME_CAPTURE,
   TRUE);
```

 

 



