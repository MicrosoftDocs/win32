---
description: This topic explains how to register a preview handler associated with a given data type.
ms.assetid: 5f194d29-d09f-4426-a63e-911db65ce700
title: How to Register a Preview Handler
ms.topic: article
ms.date: 05/31/2018
---

# How to Register a Preview Handler

This topic explains how to register a preview handler associated with a given data type. For the purposes of illustration, examples in this topic use a .xyz file type. Registration of a preview handler is a standard file association-based registration.

## Instructions

### Step 1:

First, a file name extension is associated with a ProgID. The following entry associates the **xyzfile** ProgID subkey with the .xyz file name extension.

```
HKEY_CLASSES_ROOT
   .xyz
      (Default) = [REG_SZ] xyzfile
```

The **xyzfile** ProgID subkey is stored with the other ProgIDs as shown here:

```
HKEY_CLASSES_ROOT
   xyzfile
```

Each preview handler ProgID subkey contains a subkey named **shellex** that contains a subkey *always* named **{8895b1c6-b41f-4c1c-a562-0d564250836f}**. The presence of that subkey tells the system that the handler is a preview handler.

The default value of the **{8895b1c6-b41f-4c1c-a562-0d564250836f}** subkey is the class identifier (CLSID) of your handler. An example of the **xyzfile** ProgID subkey is shown here, associating a handler of CLSID {ec3a629a-a47c-4245-bc78-b4b63d0e3154}.

```
HKEY_CLASSES_ROOT
   xyzfile
      shellex
         {8895b1c6-b41f-4c1c-a562-0d564250836f}
            (Default) = [REG_SZ] {ec3a629a-a47c-4245-bc78-b4b63d0e3154}
```

### Step 2:

Next, add the subkey under **CLSID** for your preview handler. An example is shown here. An explanation of individual entries follows.

```
HKEY_CLASSES_ROOT
   CLSID
      {ec3a629a-a47c-4245-bc78-b4b63d0e3154}
         (Default) = [REG_SZ] Fabricam XYZ Preview Handler
         DisplayName = [REG_SZ] @myhandler.dll,-101
         Icon = [REG_SZ] myhandler.dll,201
         AppID = [REG_SZ] {6d2b5079-2f0b-48dd-ab7f-97cec514d30b}
         InprocServer32
            (Default) = [REG_EXPAND_SZ] %ProgramFiles%\Fabricam\myhandler.dll
            ThreadingModel = [REG_SZ] Apartment
            ProgID = [REG_SZ] xyzfile
            VersionIndependentProgID = [REG_SZ] Version IndependentProgID
```

The default value for your subkey (here, **{ec3a629a-a47c-4245-bc78-b4b63d0e3154}**) is not required or used. However, setting it to a nonlocalized string can help you to debug registration issues.

The minus sign (-101) in the .dll resource in the DisplayName entry exists for legacy reasons. The Icon entry, on the other hand, does not require a minus sign.

The AppID value gives a reference to the AppID of the application associated with the file name extension (stored under **HKEY\_CLASSES\_ROOT**\\**APPID**. The value used here—{6d2b5079-2f0b-48dd-ab7f-97cec514d30b}—is the ID of the Prevhost.exe surrogate host. 32-bit preview handlers should use **AppID** {534A1E02-D58F-44f0-B58B-36CBED287C7C} when installed on 64-bit operating systems.

The entries under the **InprocServer32** subkey include a reference back to the file name extension's ProgID subkey as well as an entry for a [VersionIndependentProgID](../com/versionindependentprogid.md).

### Step 3:

Finally, the preview handler must be added to the list of all preview handlers. This list is used as an optimization by the system to enumerate all registered preview handlers for display purposes. Again, the default value is not required, it simply aids in the debugging process.

> [!Note]  
> In Windows 7, if the application is installed for all users of the computer, use HKEY\_LOCAL\_MACHINE; if for only one user, use HKEY\_CURRENT\_USER.

 

```
HKEY_LOCAL_MACHINE or HKEY_CURRENT_USER
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               PreviewHandlers
                  {ec3a629a-a47c-4245-bc78-b4b63d0e3154}
                     (Default) = [REG_SZ] Fabricam XYZ Preview Handler
```

## Related topics

<dl> <dt>

[Preview Handlers and Shell Preview Host](preview-handlers.md)
</dt> <dt>

[Building Preview Handlers](building-preview-handlers.md)
</dt> <dt>

[Preview Handler Guidelines](preview-handler-guidelines.md)
</dt> </dl>

 

 
