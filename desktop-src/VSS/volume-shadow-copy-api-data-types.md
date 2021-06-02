---
description: 'The following data types are defined in the Volume Shadow Copy API:'
ms.assetid: e64b36d6-4f10-42bd-9ad4-00aba90e9715
title: Volume Shadow Copy API Data Types
ms.topic: article
ms.date: 05/31/2018
---

# Volume Shadow Copy API Data Types

The following data types are defined in the Volume Shadow Copy API:

<dl> <dt>

<span id="VSS_ID"></span><span id="vss_id"></span>VSS\_ID
</dt> <dd>

``` syntax
typedef GUID VSS_ID;
```

The **VSS\_ID** definition specifies the general VSS identifier format. The **VSS\_ID** is a standard GUID data type.

**VSS\_ID**s are used to identify the following: shadow copies, shadow copy sets, providers, provider versions, writers (writer's class identifier), and instances of writers.

</dd> <dt>

<span id="VSS_PWSZ"></span><span id="vss_pwsz"></span>VSS\_PWSZ
</dt> <dd>

``` syntax
typedef /* [string][unique] */  __RPC_unique_pointer  __RPC_string WCHAR *VSS_PWSZ;
```

The **VSS\_PWSZ** definition specifies a null-terminated wide character string (wchar).

</dd> <dt>

<span id="VSS_TIMESTAMP"></span><span id="vss_timestamp"></span>VSS\_TIMESTAMP
</dt> <dd>

``` syntax
typedef LONGLONG VSS_TIMESTAMP;
```

The **VSS\_TIMESTAMP** definition holds time-stamp information as a 64-bit integer value containing the number of 100-nanosecond intervals since January 1, 1601 (UTC). This definition is interchangeable with the [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure.

</dd> </dl>

 

 
