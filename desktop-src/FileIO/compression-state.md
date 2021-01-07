---
description: Each file and directory on a volume that supports compression for individual files and directories has a compression state.
ms.assetid: 9db1b2e2-864e-45b5-8227-400cad75222e
title: Compression State
ms.topic: article
ms.date: 05/31/2018
---

# Compression State

Each file and directory on a volume that supports compression for individual files and directories has a *compression state*.

Whereas the compression attribute of a file or directory indicates simply whether the file or directory is compressed or not compressed, the compression state also specifies the format of any compressed data.

Use the [**FSCTL\_GET\_COMPRESSION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_compression) control code to determine the compression state of a file or directory.

Compression state is encoded as a 16-bit value. A compression state value of COMPRESSION\_FORMAT\_NONE indicates that a file is not compressed. A value of COMPRESSION\_FORMAT\_DEFAULT indicates that a file is compressed, using the default compression format. Any other value indicates that a file is compressed, using the compression format specified by the compression state value.

Use the [**FSCTL\_SET\_COMPRESSION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_set_compression) control code to set the compression state of a file or directory. This operation also sets the compression attribute of the file or directory.

Setting the compression state of a file to a nonzero value compresses the file, using the compression format encoded by the compression state value. Setting a file's compression state to zero decompresses the file. These are synchronous operations. The file is compressed or decompressed immediately when you set its compression state.

Setting a directory's compression state does not cause any immediate compression or decompression. Instead, setting a directory's compression state sets a default compression state that will be given to all newly created files and subdirectories.

 

 
