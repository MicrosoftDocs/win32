---
title: GetError method of the BitsClientJob class
description: The GetError method gets the error codes and error context for a BITS transfer job error.
ms.assetid: 'b18eb26f-e70f-49fb-a609-a12f4d039824'
keywords: ["GetError method", "GetError method, BitsClientJob class", "BitsClientJob class, GetError method"]
topic_type:
- apiref
api_name:
- BitsClientJob.GetError
api_location:
- Root\microsoft\bits
api_type:
- COM
---

# GetError method of the BitsClientJob class

The **GetError** method gets the error codes and error context for a BITS transfer job error.

## Syntax


```mof
uint32 GetError(
  [in]  uint32 LanguageId,
  [out] uint32 ErrorContext,
  [out] uint32 ErrorCode,
  [out] string ContextDescription,
  [out] string ErrorDescription
);
```



## Parameters

<dl> <dt>

*LanguageId* \[in\]
</dt> <dd>

Identifies the language locale used to generate the error description.

</dd> <dt>

*ErrorContext* \[out\]
</dt> <dd>

Specifies the context in which the error occurred. The following values are possible:



| Error context                                                                | Meaning                                                                                                                         |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | An error has not occurred.<br/>                                                                                           |
| <dl> <dt>1</dt> </dl> | The error context is unknown.<br/>                                                                                        |
| <dl> <dt>2</dt> </dl> | The transfer queue manager generated the error.<br/>                                                                      |
| <dl> <dt>3</dt> </dl> | The error was generated while the queue manager was notifying the client of an event.<br/>                                |
| <dl> <dt>4</dt> </dl> | The error was related to the specified local file. For example, permission was denied or the volume was unavailable.<br/> |
| <dl> <dt>5</dt> </dl> | The error was related to the remote file. For example, the URL was not accessible.<br/>                                   |
| <dl> <dt>6</dt> </dl> | The transport layer generated the error. These errors are general transport errors.<br/>                                  |
| <dl> <dt>7</dt> </dl> | The server application, to which BITS passed the upload file, generated an error while processing the upload file.<br/>   |



 

</dd> <dt>

*ErrorCode* \[out\]
</dt> <dd>

Specifies the error code that resulted in the BITS transfer job entering an error state.

</dd> <dt>

*ContextDescription* \[out\]
</dt> <dd>

Specifies the description of the context in which the error occurred.

</dd> <dt>

*ErrorDescription* \[out\]
</dt> <dd>

Specifies the description of the error code that resulted in the BITS transfer job entering an error state.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsClientJob**](bitsclientjob.md)
</dt> </dl>

 

 





