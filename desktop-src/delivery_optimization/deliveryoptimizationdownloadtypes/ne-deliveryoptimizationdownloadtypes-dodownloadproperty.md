---
title: DODownloadProperty enumeration
description: Specifies the ID of properties for the DO download operation.
keywords:
- DODownloadProperty enumeration, DODownloadProperty
topic_type:
- apiref
api_name:
- DODownloadProperty
api_location:
- deliveryoptimizationdownloadtypes.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 07/02/2019
---

# DODownloadProperty enumeration

The **DODownloadProperty** enumeration specifies the ID of properties for the DO download operation. This enumeration is used by the **IDODownload** interface, and carried out by a VARIANT value, where the type of value is contained.

## Syntax

```cpp
typedef enum _DODownloadProperty
{
  DODownloadProperty_Id = 0,
  DODownloadProperty_Uri,
  DODownloadProperty_ContentId,
  DODownloadProperty_DisplayName,
  DODownloadProperty_LocalPath,
  DODownloadProperty_HttpCustomHeaders,
  DODownloadProperty_CostPolicy,
  DODownloadProperty_SecurityFlags,
  DODownloadProperty_CallbackFreqPercent,
  DODownloadProperty_CallbackFreqSeconds,
  DODownloadProperty_NoProgressTimeoutSeconds,
  DODownloadProperty_ForegroundPriority,
  DODownloadProperty_BlockingMode,
  DODownloadProperty_CallbackInterface,
  DODownloadProperty_StreamInterface,
  DODownloadProperty_SecurityContext,
  DODownloadProperty_NetworkToken
  DODownloadProperty_CorrelationVector,
  DODownloadProperty_DecryptionInfo,
  DODownloadProperty_IntegrityCheckInfo,
  DODownloadProperty_IntegrityCheckMandatory,
  DODownloadProperty_TotalSizeBytes
} DODownloadProperty;
```

## Constants

| Requirement | Value |
|-|-|
| DODownloadProperty_Id | Read-only. Use this property to get the ID that uniquely identifies the download. VARIANT type is VT_BSTR. |
| DODownloadProperty_Uri | Use this property to set or get the remote URI path of the resource to download. This property is required only if *DODownloadProperty_ContentId* isn't provided. VARIANT type is VT_BSTR. |
| DODownloadProperty_ContentId | Use this property to set or get the download unique content ID. This property is required only if *DODownloadProperty_Uri* isn't provided. VARIANT type is VT_BSTR. |
| DODownloadProperty_DisplayName | Optional. Use this property to set or get the download display name. VARIANT type is VT_BSTR. |
| DODownloadProperty_LocalPath | Use this property to set or get the local path name to save the download file. If the path does not exist, DO will attempt to create it under the caller's privileges. This property is required only if *DODownloadProperty_StreamInterface* wasn’t provided. VARIANT type is VT_BSTR. |
| DODownloadProperty_HttpCustomHeaders | Optional. Use this property to set or get custom HTTP request headers. DO will include these headers during HTTP file request operations. The headers must already be formatted as standard HTTP headers. VARIANT type is VT_BSTR. |
| DODownloadProperty_CostPolicy | Optional. Use this property to set or get one of the **DODownloadCostPolicy** enumeration values. VARIANT type is VT_UI4. |
| DODownloadProperty_SecurityFlags | Optional write-only. Use this property to set or get the standard WinHTTP security flags (**WINHTTP_OPTION_SECURITY_FLAGS**). VARIANT type is VT_UI4.</br></br>The following flags are supported:</br>SECURITY_FLAG_IGNORE_CERT_CN_INVALID. Allows an invalid common name in a certificate.</br>SECURITY_FLAG_IGNORE_CERT_DATE_INVALID. Allows an invalid certificate date.</br>SECURITY_FLAG_IGNORE_UNKNOWN_CA. Allows an invalid certificate authority.</br>SECURITY_FLAG_IGNORE_CERT_WRONG_USAGE. Allows the identity of a server to be established with a non-server certificate.</br>WINHTTP_ENABLE_SSL_REVOCATION. Allows SSL revocation. If this flag is set, the above flags will be ignored. |
| DODownloadProperty_CallbackFreqPercent | Optional. Use this property to set or get callback frequency based on download percentage. VARIANT type is VT_UI4. |
| DODownloadProperty_CallbackFreqSeconds | Optional. Use this property to set or get callback frequency based on download time. The default is every one second. VARIANT type is VT_UI4. |
| DODownloadProperty_NoProgressTimeoutSeconds | Optional. Use this property to set or get the download timeout length for no progress. The minimum accepted value is 60 seconds of no download activity. VARIANT type is VT_UI4. |
| DODownloadProperty_ForegroundPriority | Optional. Use this property to set or get the current download priority. VARIANT_TRUE value will bring the download to the foreground with higher priority. The default is background priority. VARIANT type is VT_BOOL. |
| DODownloadProperty_BlockingMode | Optional. Use this property to set or get the current download blocking mode. VARIANT_TRUE value will cause **IDODownload::Start** to block until download is complete or error has occurred. The default is nonblocking mode. VARIANT type is VT_BOOL. |
| DODownloadProperty_CallbackInterface | Optional. Use this property to set or get the pointer to **IDODownloadStatusCallback** interface used for download callbacks. VARIANT type is VT_UNKNOWN. |
| DODownloadProperty_StreamInterface | Optional. Use this property to set or get the pointer to IStream interface used for stream download type. VARIANT type is VT_UNKNOWN. |
| DODownloadProperty_SecurityContext | Optional write-only. Use this property to set the certificate context to be used during HTTP request operations. The value must consist of serialized bytes of CERT_CONTEXT. VARIANT type is (VT_ARRAY \| VT_UI1). |
| DODownloadProperty_NetworkToken | Optional write-only. Use this property to set the network token to be used during HTTP operations. VARIANT_TRUE value will cause DO to capture the caller's identity token and VARIANT_FALSE will clear the existing token. The default is the token of the logged-on user. VARIANT type is VT_BOOL. |
| DODownloadProperty_CorrelationVector | Optional. Sets a specific correlation vector for telemetry purposes. VARIANT type is VT_BSTR. |
| DODownloadProperty_DecryptionInfo | Optional write-only. Sets decryption information in the form of a JSON string. VARIANT type is VT_BSTR. |
| DODownloadProperty_IntegrityCheckInfo | Optional write-only. Sets the piece hash file (PHF) location, which is used by DO to perform runtime integrity checks on the downloaded content. VARIANT type is VT_BSTR. |
| DODownloadProperty_IntegrityCheckMandatory | Optional. Sets a Boolean flag indicating whether usage of the piece hash file (PHF) is mandatory. If VARIANT_TRUE, the download will be aborted if the integrity check fails. VARIANT type is VT_BOOL. |
| DODownloadProperty_TotalSizeBytes | Optional. Specifies the total download size in bytes. VARIANT type is VT_UI8. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | DeliveryOptimizationDownloadTypes.h |
