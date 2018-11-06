---
title: Surrogate Sharing
description: DLL servers will share a surrogate if they have matching security identities and share the same AppID value.
ms.assetid: 88544be1-4716-47b6-9c08-2b5b2b178e1f
ms.topic: article
ms.date: 05/31/2018
---

# Surrogate Sharing

DLL servers will share a surrogate if they have matching security identities and share the same AppID value.

DLL servers are loaded, by default, into their own surrogate process. To load other DLL servers into an existing surrogate so that it supports more than one DLL server, there are two requirements:

-   The DLL servers must have the same AppID value.
-   The security context of the DLL servers must be the same.

If two DLL servers are to be launched under different security identities, they must be in different surrogates, whether their AppIDs match.

Following is an example of administering surrogate sharing with AppIDs:

``` syntax
    AppID
        {12345678-0000-0000-0000-abcdabcdabcd}
            @DllSurrogate    REG_SZ
    CLSID
        {12345678-0000-0000-0000-000000000001}
            @AppId    REG_SZ    {12345678-0000-0000-0000-abcdabcdabcd}
            InProcServer32
    @    REG_SZ    c:\myapp\comp1.dll
        {12345678-0000-0000-0000-000000000002}
            @AppId    REG_SZ    {12345678-0000-0000-0000-abcdabcdabcd}
            InProcServer32
    @    REG_SZ    c:\myapp\comp2.dll
 
```

The two CLSIDs for DLL components comp1.dll and comp2.dll have been configured to share an AppID. The [AppID](appid-key.md) key specifies that the DLL server can be loaded in a surrogate by specifying the [DllSurrogate](dllsurrogate.md) value. In this example, the **DllSurrogate** value is an empty string, indicating that the default system implementation of the DLL surrogate should be used.

## Related topics

<dl> <dt>

[DLL Server Requirements](dll-server-requirements.md)
</dt> <dt>

[Registering the DLL Server for Surrogate Activation](registering-the-dll-server-for-surrogate-activation.md)
</dt> </dl>

 

 




