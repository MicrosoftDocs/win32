---
description: Describes the enterprise protection state of a file or folder.
title: FileProtectionStatus enumeration
ms.topic: reference
ms.date: 01/22/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FileProtectionStatus
api_type: 
- HeaderDef
api_location: 
- None
---

# FileProtectionStatus enumeration

Describes the enterprise protection state of a file or folder.

## Syntax


```C++
typedef enum {
    Undetermined = 0,
    Unprotected,
    Protected,
    ProtectedByOtherUser,
    ProtectedToOtherEnterprise,
    NotProtectable,
    ProtectedToOtherIdentity,
    LicenseExpired,
    AccessSuspended,
    FileInUse
} FileProtectionStatus;
```

## Constants

### Unknown:0

The item is either encrypting or decrypting and the enterprise protection status cannot be determined. Check again later.

### Undetermined:0

> [!NOTE]
> **Undetermined** may be unavailable for releases after Windows 10. Instead, use **Unknown**.

The item is either encrypting or decrypting and the enterprise protection status cannot be determined. Check again later.

### Unprotected:1

The item is not protected using enterprise protection.

### Revoked:2

The item has been revoked using enterprise protection.

### Protected:3

The item is protected using enterprise protection and you're app can open this file because it is on the allowed list of the policy.

### ProtectedByOtherUser:4

> [!NOTE]
> **ProtectedByOtherUser** may be unavailable for releases after Windows 10. Instead, use **ProtectedToOtherIdentity**.

Another user has protected the item using enterprise protection.

### ProtectedToOtherEnterprise:5

> [!NOTE]
> **ProtectedToOtherEnterprise** may be unavailable for releases after Windows 10. Instead, use **ProtectedToOtherIdentity**.

The item is protected for another enterprise id using enterprise protection.

### NotProtectable:6

The item is encrypted or is a system file and cannot be protected using enterprise protection.

### ProtectedToOtherIdentity:7

The item is protected for another enterprise identity using enterprise protection.

### LicenseExpired:8

The item's RMS license has expired.

### AccessSuspended:9

The keys to access the protected item have been dropped while the device is locked.

### FileInUse:10

The item is being used by another process. You can apply enterprise protection to it only after it becomes exclusively available.




## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |




 

 




