---
description: "Learn more about: Callback Parameters"
title: Callback Parameters
TOCTitle: Callback Parameters
ms:assetid: 7f3cdc13-ffbd-4e5a-b650-1c6388e784dc
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269310(v=EXCHG.10)
ms:contentKeyID: 32765600
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# Callback Parameters


_**Applies to:** Windows | Windows Server_

## Callback Parameters

This topic contains parameters that are used for callbacks.

*JET_paramDisableCallbacks*  
65  

This parameter disables all database engine callbacks to application provided functions. It is primarily intended to support the database engine utilities and is not intended to be used in your application.


| 
|
| <p>Default Value:</p> | <p>False</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramEnablePersistedCallbacks*  
156  

This parameter enables the use of persistent callbacks in the database. In releases prior to Windows Vista, the use of persistent callbacks was enabled by default. Applications must now explicitly enable the use of persistent callbacks at runtime using this parameter. If this parameter is not set, then any database operation that requires the invocation of a callback will fail with JET_errCallbackFailed. This parameter does not affect any callbacks that are specified at runtime with the following mechanisms: JET_paramRuntimeCallback, [JetRegisterCallback](./jetregistercallback-function.md), or an explicit callback parameter to a JET API. It is still possible to create schema elements that contain persistent callbacks even when the use of those persistent callbacks is disallowed. When this parameter is set to false it overrides JET_paramDisableCallbacks.


| 
|
| <p>Default Value:</p> | <p>False</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows Vista and later releases</p> | 



*JET_paramRuntimeCallback*  
73  

This parameter configures the engine with a runtime callback function implementing the [JET_CALLBACK](./jet-callback-callback-function.md) interface. This callback may be called for the following reasons: [JET_cbtypFreeCursorLS](./jet-cbtyp.md), [JET_cbtypFreeTableLS](./jet-cbtyp.md), or [JET_cbtypNull](./jet-cbtyp.md). Please see [JetSetLS](./jetsetls-function.md) for more information.


| 
|
| <p>Default Value:</p> | <p>NULL</p> | 
| <p>Type:</p> | <p>Function Pointer (JET_API_PTR)</p> | 
| <p>Valid Range:</p> | <p>NULL, <a href="gg294098(v=exchg.10).md">JET_CALLBACK</a>*</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_API_PTR](./jet-api-ptr.md)  
[JET_CALLBACK](./jet-callback-callback-function.md)  
[JET_CBTYP](./jet-cbtyp.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)  
[JetSetLS](./jetsetls-function.md)
