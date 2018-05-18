---
title: BitsClientJob class
description: The BitsClientJob class provides methods to manage Background Intelligent Transfer Service (BITS) transfer jobs.
ms.assetid: '9eb1009f-395e-42cf-a981-f219dafc0584'
keywords: ["BitsClientJob class", "BitsClientJob class, described"]
topic_type:
- apiref
api_name:
- BitsClientJob
- BitsClientJob.JobId
- BitsClientJob.DisplayName
- BitsClientJob.Description
- BitsClientJob.Priority
- BitsClientJob.MinimumRetryDelay
- BitsClientJob.NoProgressTimeout
- BitsClientJob.Files
- BitsClientJob.JobCreationTime
- BitsClientJob.JobLastModificationTime
- BitsClientJob.JobCompletionTime
- BitsClientJob.BytesTotal
- BitsClientJob.BytesTransferred
- BitsClientJob.FilesTotal
- BitsClientJob.FilesTransferred
- BitsClientJob.TransientErrorCount
- BitsClientJob.State
- BitsClientJob.Owner
api_location:
- Root\microsoft\bits
api_type:
- Schema
---

# BitsClientJob class

The **BitsClientJob** class provides methods to manage Background Intelligent Transfer Service (BITS) transfer jobs.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetical order, not MOF order.

## Syntax

``` syntax
[Provider("BitsClientProv"), Dynamic]
class BitsClientJob
{
  string         JobId;
  string         DisplayName;
  string         Description;
  uint32         Priority;
  uint32         MinimumRetryDelay;
  uint32         NoProgressTimeout;
  BitsClientFile Files[];
  uint64         JobCreationTime;
  uint64         JobLastModificationTime;
  uint64         JobCompletionTime;
  uint64         BytesTotal;
  uint64         BytesTransferred;
  uint32         FilesTotal;
  uint32         FilesTransferred;
  uint32         TransientErrorCount;
  uint16         State;
  string         Owner;
};
```

## Members

The **BitsClientJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **BitsClientJob** class has these methods.



| Method                                                                         | Description                                                                                                                                 |
|:-------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddFile**](addfile-bitsclientjob.md)                                       | Adds a file to an existing BITS transfer job.<br/>                                                                                    |
| [**CreateJob**](createjob-bitsclientjob.md)                                   | Creates a BITS transfer job.<br/>                                                                                                     |
| [**GetError**](geterror-bitsclientjob.md)                                     | Gets the error codes and error context for a BITS transfer job error.<br/>                                                            |
| [**RemoveClientCertificate**](removeclientcertificate-bitsclientjob.md)       | Removes the client certificate from the job.<br/>                                                                                     |
| [**RemoveCredentials**](removecredentials-bitsclientjob.md)                   | Removes the credentials from the *useTarget* parameter. <br/>                                                                         |
| [**SetClientCertificateById**](setclientcertificatebyid-bitsclientjob.md)     | Sets the client certificate to use for client authentication in an HTTPS (SSL) request. <br/>                                         |
| [**SetClientCertificateByName**](setclientcertificatebyname-bitsclientjob.md) | Sets the client certificate to use for client authentication in an HTTPS (SSL) request.<br/>                                          |
| [**SetCredentials**](setcredentials-bitsclientjob.md)                         | Identifies the *Target* parameter, the authentication scheme, and the user credentials to use for user authentication requests. <br/> |
| [**SetJobState**](setjobstate-bitsclientjob.md)                               | Changes the state of a BITS transfer job.<br/>                                                                                        |
| [**SetProxySettings**](createjob-bitsclientjob.md)                            | Modifies the proxy settings for a BITS transfer job.<br/>                                                                             |



 

### Properties

The **BitsClientJob** class has these properties.

<dl> <dt>

**BytesTotal**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the total number of bytes to transfer for all the files in the BITS transfer job.

</dd> <dt>

**BytesTransferred**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the number of bytes that were transferred.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property specifies the description of the BITS transfer job.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property specifies the name of the BITS transfer job.

</dd> <dt>

**Files**
</dt> <dd> <dl> <dt>

Data type: **BitsClientFile** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property gets the list of files that were added to the BITS transfer job.

</dd> <dt>

**FilesTotal**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the total number of files to transfer for this BITS transfer job.

</dd> <dt>

**FilesTransferred**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the number of files transferred.

</dd> <dt>

**JobCompletionTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the time when the BITS transfer job entered the completed state. The *HighDateTime* parameter is in most significant bits (MSB), and the *LowDateTime* parameter is in least significant bits (LSB).

</dd> <dt>

**JobCreationTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the creation time of the BITS transfer job. The *HighDateTime* parameter is in MSB, and the *LowDateTime* parameter is in LSB.

</dd> <dt>

**JobId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the **GUID** that is associated with the BITS transfer job.

</dd> <dt>

**JobLastModificationTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the last modification time of the BITS transfer job. The *HighDateTime* parameter is in MSB, and the *LowDateTime* parameter is in LSB.

</dd> <dt>

**MinimumRetryDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property specifies the minimum time that BITS waits before it tries to transfer the file after a transient error condition occurs.

</dd> <dt>

**NoProgressTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property specifies the length of time that the service tries to transfer the file after a transient error condition occurs. If there is progress, the timer is reset.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the owner of the BITS transfer job.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property specifies the priority of the BITS transfer job.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the state of the BITS transfer job.

</dd> <dt>

**TransientErrorCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the number of times that a transit error occurred for the BITS transfer job.

</dd> </dl>

## Remarks

If a BITS transfer job exists that was created by a user who no longer exists on the computer, job enumerations fail with **WBEM\_E\_FAILED** error code.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



 

 





