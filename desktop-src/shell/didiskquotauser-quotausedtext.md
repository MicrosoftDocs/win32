---
Description: Gets the user's current disk usage as a text string.
title: DIDiskQuotaUser.QuotaUsedText property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DIDiskQuotaUser.QuotaUsedText property

Gets the user's current disk usage as a text string.

This property is read-only.

## Syntax


```JScript
QuotaUsedText = DIDiskQuotaUser.QuotaUsedText
```



## Property value

A string value that is set to the amount of disk space currently in use. If NTFS file compression is enabled, this property reflects the amount of disk space that the data would require in an uncompressed state.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DIDiskQuotaUser Object**](didiskquotauser-object.md)
</dt> <dt>

[**QuotaLimitText**](didiskquotauser-quotalimittext.md)
</dt> <dt>

[**QuotaThresholdText**](didiskquotauser-quotathresholdtext.md)
</dt> <dt>

[**QuotaUsed**](didiskquotauser-quotaused.md)
</dt> </dl>

 

 




