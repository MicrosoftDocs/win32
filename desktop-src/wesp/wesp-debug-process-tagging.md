---
title: Test and validate your code with the Windows endpoint security platform
description: Configure and validate Windows endpoint security platform process tagging by inspecting the WESP permission claim on a process token.
author: jgeurten
ms.author: jogeurte
ms.topic: troubleshooting
ms.date: 10/06/2026
ai-usage: ai-assisted
---

# Test and validate your code with the Windows endpoint security platform (WESP)

The Windows endpoint security platform (WESP) requires your components to be code signed and pass the WESP policy in Windows. Components that pass policy will be tagged by Windows with the `WESP://Permission` security attribute on a process token.  

Use this article to test on the WESP platform and verify the `WESP://Permission` security attribute on your process token. This procedure can be followed to validate your component is configured correctly to interact with the platform without having to retail sign the component and without your Artifact Signing identity allowlisted in the WESP policy. The procedure uses a test-signed Image File Execution Options (IFEO) value to assign a permission mask to an executable. Code Integrity adds the corresponding claim when it validates a new instance of that executable.

> [!WARNING]
> Use this procedure only on an isolated test device or virtual machine. It requires security configuration changes that aren't appropriate for production devices, including test signing, disabled Secure Boot, and potentially disabled memory integrity. Restore the original security configuration after testing.

## Prerequisites

Before you begin, prepare the following environment:

- Use a supported Windows build as described in [Windows endpoint security platform requirements, signing, and enrollment](wesp-requirements.md).
- Install [WinDbg](/windows-hardware/drivers/debugger/) on the host computer.
- Configure a host and target for [kernel debugging over Ethernet](/windows-hardware/drivers/debugger/setting-up-a-network-debugging-connection-automatically).
- An executable linked with [`/INTEGRITYCHECK`](/cpp/build/reference/integritycheck). The executable must have a valid signature from a signer in the local machine's **Trusted Root Certification Authorities** and **Trusted Publishers** stores.
- [Disable Secure Boot](/windows-hardware/manufacture/desktop/disabling-secure-boot/) on the test target so that you can enable test signing.
- If memory integrity is enabled, disable it for this test. The debug tagging path described in this article doesn't run when Code Integrity validation occurs in the virtualization-based security environment.

## Enable test signing

Enable test signing from an elevated Command Prompt:

```cmd
bcdedit /set testsigning on
```

Restart the target, and then verify the setting:

```cmd
bcdedit /enum {current} | findstr /i testsigning
```

The output should contain:

```output
testsigning             Yes
```

If `bcdedit` reports that the value is protected by Secure Boot policy, confirm that Secure Boot is disabled.

## Confirm that the executable is integrity checked

The WESP tagging feature only runs when Code Integrity performs cryptographic image validation. Executables linked with `/INTEGRITYCHECK` use this validation path. Most ordinary desktop executables and packaged apps don't use this path during process creation.

Use either of the following methods to confirm that the executable has the `IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY` flag.

### Check the PE headers with Linker Tools

From a Visual Studio Developer Command Prompt, run:

```cmd
link /dump /headers C:\Path\To\YourExecutable.exe
```

Under `DLL characteristics`, verify that the output includes `Check integrity`.

### Check the PE headers with PowerShell

Run the following PowerShell script:

```powershell
$path = 'C:\Path\To\YourExecutable.exe'
$bytes = [System.IO.File]::ReadAllBytes($path)
$peOffset = [BitConverter]::ToInt32($bytes, 0x3C)
$dllCharacteristics = [BitConverter]::ToUInt16($bytes, $peOffset + 24 + 0x46)

'DllCharacteristics = 0x{0:X4}; IntegrityCheck = {1}' -f `
    $dllCharacteristics, [bool]($dllCharacteristics -band 0x0080)
```

An `IntegrityCheck` value of `True` confirms that the executable has the integrity-check flag.

## Configure the debug permission

Create a `WespPermissions` `REG_DWORD` value under the executable's IFEO key. The key uses the image file name, not the full path.

Replace `YourExecutable.exe` with the image file name of your integrity-checked executable. From an elevated Command Prompt, assign the permission mask `0x01` to new instances of the executable:

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\YourExecutable.exe" /v WespPermissions /t REG_DWORD /d 0x01 /f
```

Verify the value:

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\YourExecutable.exe" /v WespPermissions
```

The result should show `WespPermissions` as a `REG_DWORD` with the value `0x1`.

> [!IMPORTANT]
> Process tagging occurs during process creation. Close any existing instance of the target, and then start a new instance after you set or change `WespPermissions`.

## Start the target process

Start your integrity-checked executable and leave it running while you inspect its token.

## Inspect the process token

Connect the kernel debugger to the target, break into the target, and then complete these steps at the `kd>` prompt:

1. Find the current process object:

   ```text
   !process 0 0 YourExecutable.exe
   ```

1. Copy the `PROCESS` address from the output, and then display the process details:

   ```text
   !process <ProcessAddress>
   ```

1. Copy the address from the `Token` line, and then display the token:

   ```text
   !token <TokenAddress>
   ```

1. Find `WESP://Permission` under `Security Attributes`.

A successful result resembles the following output:

```output
Security Attributes:
 01 Claim Name  : WESP://Permission
    Claim Flags : 0x41 - UNKNOWN
    Value Type  : CLAIM_SECURITY_ATTRIBUTE_TYPE_OCTET_STRING
    Value Count : 1
    Value[0]    : 01 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00
```

The `WESP://Permission` attribute confirms that Code Integrity tagged the process.

## Interpret the permission claim

The value is a 16-byte `WESP_CLAIMS_V1` octet string. Interpret each four-byte field as a little-endian unsigned integer.

| Bytes | Field | Meaning in the example |
|---|---|---|
| `01 00 00 00` | Version | Claim format version 1. |
| `01 00 00 00` | Permissions | The `0x01` value configured in `WespPermissions`. |
| `01 00 00 00` | Debug attributes | The permission came from the IFEO debug path. |
| `00 00 00 00` | Reserved | Reserved value 0. |

The debugger might display claim flags as `0x41 - UNKNOWN`. This value doesn't indicate that validation failed.

## Troubleshoot process tagging

Use the following guidance if the expected claim isn't present.

### The target isn't integrity checked

If `Check integrity` or `IntegrityCheck = True` isn't present, Code Integrity won't use the required validation path when the process is created. Link the executable with `/INTEGRITYCHECK`, sign it again, and repeat the test.

### Memory integrity is enabled

The IFEO debug-tagging path described in this article doesn't run when memory integrity performs Code Integrity validation in the virtualization-based security environment. Test on an isolated system with memory integrity disabled, and restore the setting after testing.

### The custom executable fails with status 0xC0000428

An executable linked with `/INTEGRITYCHECK` must have a valid signature from a signer that the target trusts. Confirm that:

- Test signing is enabled and the target was restarted.
- The test certificate is installed in the target's local machine **Trusted Root Certification Authorities** and **Trusted Publishers** stores.
- The executable was signed after its final build.

### The token is from the wrong process

Run `!process 0 0 <ImageName>` again and use the current process address. Don't use a stale process address or `!token 0`.

### Symbols don't resolve

Configure WinDbg to use the [Microsoft public symbol server](/windows-hardware/drivers/debugger/microsoft-public-symbols), and then reload symbols:

```text
.symfix C:\symbols
.reload /f
```

Use symbols that match the exact target build. Prerelease builds might require symbols supplied with that build.

### The registry value is correct, but the claim is absent

Confirm each prerequisite:

- The Windows build supports WESP process tagging.
- `bcdedit /enum {current}` reports `testsigning Yes`.
- Memory integrity is disabled for the test.
- The IFEO key uses only the image file name.
- `WespPermissions` is a `REG_DWORD`.
- The target executable is integrity checked.
- You started a new process after configuring the registry value.

## Clean up the test configuration

Restore the security protections disabled for this test:

1. Close the target process. From an elevated Command Prompt, remove the debug permissions and disable test signing:

   ```cmd
   reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\YourExecutable.exe" /v WespPermissions /f
   bcdedit /set testsigning off
   ```

2. Restart the system. Restore Secure Boot to its original setting in the firmware menu and memory integrity to its original setting in Windows Security. Restart again if prompted, and verify both settings.