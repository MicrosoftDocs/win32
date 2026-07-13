---
title: Create Process In Sandbox APIs
description: Creates a new process in a composable sandbox.
ms.tgt_platform: multiple
keywords:
- CreateProcessInSandbox
topic_type:
- apiref
api_name:
- Experimental_CreateProcessInSandbox
- Experimental_CreateProcessAsUserInSandbox
api_location:
- processmodel.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 6/1/2026
---

# Create Process in Sandbox

Creates a new process in a composable sandbox.

This article documents both **Experimental_CreateProcessInSandbox** and **Experimental_CreateProcessAsUserInSandbox**. These APIs launch a process with the containment properties described by a compiled sandbox specification. They are the sandboxed equivalents of [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw) and [**CreateProcessAsUser**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasuserw), respectively.

> [!IMPORTANT]
> These APIs are experimental and subject to change.

## Syntax

```cpp
BOOL Experimental_CreateProcessInSandbox(
    _In_opt_  LPCWSTR                applicationName,
    _Inout_opt_ LPWSTR               commandLine,
    _In_opt_  LPSECURITY_ATTRIBUTES  processAttributes,      // Reserved
    _In_opt_  LPSECURITY_ATTRIBUTES  threadAttributes,       // Reserved
    BOOL                             inheritHandles,          // Reserved
    DWORD                            creationFlags,
    _In_opt_  LPVOID                 environment,
    _In_opt_  LPCWSTR                currentDirectory,
    _In_      LPSTARTUPINFOW         startupInfo,
    _In_      LPCWSTR                identity,
    _In_reads_bytes_(sandboxSpecificationSize) LPCVOID sandboxSpecification,
    DWORD                            sandboxSpecificationSize,
    _Out_     LPPROCESS_INFORMATION  processInformation
);
```

```cpp
BOOL Experimental_CreateProcessAsUserInSandbox(
    _In_      HANDLE                 token,
    _In_opt_  LPCWSTR                applicationName,
    _Inout_opt_ LPWSTR               commandLine,
    _In_opt_  LPSECURITY_ATTRIBUTES  processAttributes,      // Reserved
    _In_opt_  LPSECURITY_ATTRIBUTES  threadAttributes,       // Reserved
    BOOL                             inheritHandles,          // Reserved
    DWORD                            creationFlags,
    _In_opt_  LPVOID                 environment,
    _In_opt_  LPCWSTR                currentDirectory,
    _In_      LPSTARTUPINFOW         startupInfo,
    _In_      LPCWSTR                identity,
    _In_reads_bytes_(sandboxSpecificationSize) LPCVOID sandboxSpecification,
    DWORD                            sandboxSpecificationSize,
    _Out_     LPPROCESS_INFORMATION  processInformation
);
```

## Parameters

### `token` (AsUser variant only)

A handle to the primary token that represents the user under whose identity the sandboxed process will run. The handle must have `TOKEN_QUERY`, `TOKEN_DUPLICATE`, and `TOKEN_ASSIGN_PRIMARY` access.

Same as [**CreateProcessAsUser**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasuserw).

If this parameter is **NULL**, the function fails with `E_HANDLE`.

---

### `applicationName`

Same as [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw). If NULL, the executable is resolved from `commandLine`.

---

### `commandLine`

Same as [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw).

---

### `processAttributes`

> **Not supported.** Must be **NULL**. If non-NULL, the function fails with `ERROR_NOT_SUPPORTED`. This parameter is reserved for future use.

---

### `threadAttributes`

> **Not supported.** Must be **NULL**. If non-NULL, the function fails with `ERROR_NOT_SUPPORTED`. This parameter is reserved for future use.

---

### `inheritHandles`

> **Not supported.** Must be **FALSE**. If TRUE, the function fails with `ERROR_NOT_SUPPORTED`. This parameter is reserved for future use.

---

### `creationFlags`

Same as [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw).

> **Important:** If you supply an `environment` block, you **must** include `CREATE_UNICODE_ENVIRONMENT` in `creationFlags`. Only Unicode environment blocks are accepted (see *environment* below).

---

### `environment`

Same as [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw).

**Additional constraints:**

| Constraint | Error |
|---|---|
| Must be a **Unicode** (wide-character) environment block. ANSI environment blocks are not supported. | `E_INVALIDARG` |
| Must be WCHAR-aligned (size must be a multiple of `sizeof(WCHAR)`). | `E_INVALIDARG` |
| Must be double-null terminated (`L"\0\0"` at end). | `E_INVALIDARG` |
| Maximum size: 32 MB. | `E_INVALIDARG` |

If NULL, the child process inherits the environment of the calling process (standard `CreateProcess` behavior).

---

### `currentDirectory`

Same as [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw). If NULL, defaults to the caller's current directory.

---

### `startupInfo`

Same as [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw).

Must not be NULL. If NULL, the function fails with `E_INVALIDARG`.

---

### `identity`

A null-terminated Unicode string that uniquely identifies this sandbox instance. The identity serves as the **AppContainer profile name** (when AppContainer isolation is enabled) and determines the process identity SID on the token.

**Requirements:**

- Must not be NULL. If NULL, the function fails with `E_INVALIDARG`.
- Must uniquely identify the sandbox. Two sandboxes with the same identity share an AppContainer profile (and therefore share filesystem/network permissions derived from that profile).
- Must **not** collide with an installed MSIX package family name. The engine rejects identities whose package family name matches a currently installed MSIX package (error: `E_ACCESSDENIED`). This protects against sandbox processes inheriting permissions meant for an installed app.
  - **Developer bypass:** This check is skipped when the system has Developer Mode enabled, Secure Boot disabled, and Test Signing enabled.

**Examples:**

```
"MyAgent_Sandbox_001"
"Contoso.ChatBot_abc123"
```

---

### `sandboxSpecification`

A pointer to a compiled sandbox specification buffer (FlatBuffer format, file identifier `"SBOX"`).

Must not be NULL. If NULL (or `sandboxSpecificationSize` is 0), the function fails with `E_INVALIDARG`.

The specification describes the containment properties to apply to the launched process. See [Sandbox Specification Fields](#sandbox-specification-fields) below.

---

### `sandboxSpecificationSize`

The size, in bytes, of the `sandboxSpecification` buffer.

---

### `processInformation`

Same as [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw).

Must not be NULL. If NULL, the function fails with `E_INVALIDARG`.

---

## Return Value

If the function succeeds, the return value is nonzero (TRUE).

If the function fails, the return value is zero (FALSE). Call `GetLastError` to retrieve the extended error code.

---

## Sandbox Specification Fields

The sandbox specification is a FlatBuffer-encoded structure (schema: `SandboxSpec.fbs`) that describes containment policies. The following fields are supported:

### `version` (string, **required**)

Schema version. Must be `"0.1.0"` for the current release. The engine rejects any other version with `ERROR_NOT_SUPPORTED`.

---

### `app_container` (bool, default: `false`)

Enables **AppContainer** isolation for the sandboxed process. When true, the engine creates (or opens) an AppContainer profile using the `identity` parameter as the profile name, and launches the process within that AppContainer.

AppContainer provides:
- Kernel-level process isolation (default-deny access to most system resources)
- Network isolation (no network access unless granted via capabilities)
- Filesystem isolation (no access outside explicitly granted paths)

> **Important:** Many sandbox restriction fields -- including `fs_read_write`, `fs_read_only`, `network_policy`, and `capabilities` -- **do not take effect** if `app_container` is `false`. These features rely on AppContainer isolation as the underlying enforcement mechanism. Setting filesystem paths or capabilities without AppContainer will result in `E_INVALIDARG`.

---

### `integrity` (enum IntegrityLevel, default: `system_default`)

Controls the integrity level of the sandboxed process token.

| Value | Behavior |
|---|---|
| `system_default` | The system chooses a secure default. For AppContainer processes this is **Low** integrity; for non-AppContainer processes, standard `CreateProcess` inheritance applies. |
| `inherit` | The child process inherits the caller's integrity level (classic `CreateProcess` behavior). |
| `untrusted` | Sets the process to **Untrusted** integrity level. |
| `low` | Sets the process to **Low** integrity level (`SECURITY_MANDATORY_LOW_RID`). |
| `medium` | Sets the process to **Medium** integrity level (`SECURITY_MANDATORY_MEDIUM_RID`). |
| `high` | Sets the process to **High** integrity level (`SECURITY_MANDATORY_HIGH_RID`). |

> **Note:** When `app_container` is enabled, the integrity level is always **Low** (`system_default` behavior). Explicitly setting a different integrity level in combination with `app_container = true` is not supported.

**Security constraint:** The engine refuses to set an integrity level **higher** than the caller's token integrity level (error: `E_ACCESSDENIED`). You cannot escalate privilege via this field.

---

### `disallow_win32k_system_calls` (bool, default: `false`)

When true, applies the **Win32k System Call Disable** mitigation policy. The sandboxed process is completely denied access to the GUI subsystem (win32k.sys). This is appropriate for headless/background workloads.

---

### `ui_restrictions` (uint64, default: `0`)

A bitmask of `JOB_OBJECT_UILIMIT_*` flags that restrict the sandboxed process's interaction with the Windows desktop. The process is placed in a Job Object with these UI restrictions applied.

> **Job hierarchy impact:** The sandboxed process is assigned to a new Job Object created by the system. If the calling process (or its process tree) is already associated with a Job Object, be aware that Windows Job Object nesting rules apply. The new Job becomes a child in the job hierarchy. Limits set on a parent job still apply to all processes in child jobs. Callers that rely on their own job hierarchy should account for the additional job created here.

A value of `0` means no UI restrictions. Common flags include:

| Flag | Value | Description |
|---|---|---|
| `JOB_OBJECT_UILIMIT_DESKTOP` | `0x0040` | Prevents creating or switching desktops. |
| `JOB_OBJECT_UILIMIT_DISPLAYSETTINGS` | `0x0010` | Prevents changing display settings. |
| `JOB_OBJECT_UILIMIT_EXITWINDOWS` | `0x0080` | Prevents calling `ExitWindowsEx`. |
| `JOB_OBJECT_UILIMIT_GLOBALATOMS` | `0x0020` | Restricts global atom access. |
| `JOB_OBJECT_UILIMIT_HANDLES` | `0x0001` | Restricts access to USER handles outside the job. |
| `JOB_OBJECT_UILIMIT_READCLIPBOARD` | `0x0002` | Prevents reading the clipboard. |
| `JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS` | `0x0008` | Prevents changing system parameters. |
| `JOB_OBJECT_UILIMIT_WRITECLIPBOARD` | `0x0004` | Prevents writing to the clipboard. |

---

### `capabilities` (string, default: empty)

A comma-delimited list of named capabilities to grant to the sandboxed process (e.g., `"internetClient,registryRead"`).

> **Requires `app_container = true`.** If capabilities are specified without AppContainer enabled, the function fails with `E_INVALIDARG`.

Capabilities are resolved via `DeriveCapabilitySidsFromName`. If any requested capability cannot be resolved, the **entire operation fails** -- the engine does not silently degrade the sandbox (that would grant a weaker sandbox than the caller intended).

**Common capabilities:**

| Capability | Description |
|---|---|
| `internetClient` | Outbound network access to the Internet. |
| `internetClientServer` | Inbound and outbound Internet network access. |
| `privateNetworkClientServer` | Home/work network access. |
| `registryRead` | Read access to HKLM registry hives. |

---

### `fs_read_write` (array of strings, default: empty)

An array of directory paths to which the sandboxed process is granted **read/write** access via Bound File System (BFS) policies.

> **Requires `app_container = true`.** If filesystem paths are specified without AppContainer, the function fails with `E_INVALIDARG`.

Paths should be fully qualified (e.g., `"C:\\Users\\Alice\\Documents\\Workspace"`). Access is applied **recursively** to all files and subdirectories under the specified path.

> **Exception:** When a read/write path is set to a drive root (e.g., `"C:\\"`) the access grant does **not** apply recursively. Only the root directory itself is accessible, not the entire volume.

---

### `fs_read_only` (array of strings, default: empty)

An array of directory paths to which the sandboxed process is granted **read-only** access via Bound File System (BFS) policies.

> **Requires `app_container = true`.** If filesystem paths are specified without AppContainer, the function fails with `E_INVALIDARG`.

Paths should be fully qualified. Access is applied **recursively** to all files and subdirectories under the specified path.

---

### `network_policy` (table NetworkPolicy, default: empty)

Network policy configuration for the sandboxed process.

> **Requires `app_container = true`.** Network policy relies on AppContainer network isolation.

#### `network_policy.proxy` (table proxy_info)

##### `proxy.url` (string)

A URL specifying the proxy server through which the sandboxed process's network traffic is routed. When set, the engine configures the AppContainer's proxy settings so that all outbound traffic flows through the specified proxy.

---

## Additional Restrictions

### Impersonation Restriction

The SandboxEngine enforces that the caller's **process token** and **thread token** (impersonation context) refer to the same identity. If the caller is impersonating a different user at the time of the call, the function fails with `ERROR_NOT_SAME_OBJECT`.

This prevents a service from creating a sandbox under the wrong user's identity when impersonating on behalf of multiple clients.

### AppContainer Callers Blocked

A process that is itself running inside an AppContainer **cannot** call these APIs. The engine rejects such calls with `E_ACCESSDENIED`. The threat model for nested sandbox composition (AppContainer creating a child sandbox) is not yet finalized.

---

## Remarks

- The APIs are exported from `processmodel.dll`. Callers should load the library dynamically:

  ```cpp
  HMODULE hMod = LoadLibraryExW(L"processmodel.dll", NULL, LOAD_LIBRARY_SEARCH_SYSTEM32);
  auto pfn = (PFN_Experimental_CreateProcessInSandbox)GetProcAddress(hMod, "Experimental_CreateProcessInSandbox");
  ```

- The sandbox specification buffer is a FlatBuffer binary blob (file identifier `"SBOX"`) conforming to the `SandboxSpec.fbs` schema.

- The `Experimental_CreateProcessAsUserInSandbox` variant allows specifying a different user token (similar to `CreateProcessAsUser`). The `identity` parameter must still be supplied.

---

## Error Codes

| Condition | Error |
|---|---|
| `processAttributes` is non-NULL | `ERROR_NOT_SUPPORTED` |
| `threadAttributes` is non-NULL | `ERROR_NOT_SUPPORTED` |
| `inheritHandles` is TRUE | `ERROR_NOT_SUPPORTED` |
| `token` is NULL (AsUser variant) | `E_HANDLE` |
| `startupInfo` is NULL | `E_INVALIDARG` |
| `sandboxSpecification` is NULL or size is 0 | `E_INVALIDARG` |
| `processInformation` is NULL | `E_INVALIDARG` |
| `identity` is NULL | `E_INVALIDARG` |
| Environment block not WCHAR-aligned | `E_INVALIDARG` |
| Environment block missing double-null terminator | `E_INVALIDARG` |
| Environment block exceeds 32 MB | `E_INVALIDARG` |
| Spec `version` is not `"0.1.0"` | `ERROR_NOT_SUPPORTED` |
| FlatBuffer verification fails | `ERROR_INVALID_DATA` |
| Capabilities specified without `app_container` | `E_INVALIDARG` |
| Filesystem paths specified without `app_container` | `E_INVALIDARG` |
| Proxy specified without `app_container` | `E_INVALIDARG` |
| Identity collides with installed MSIX package | `E_ACCESSDENIED` |
| Impersonation mismatch (process token != thread token) | `ERROR_NOT_SAME_OBJECT` |
| Caller is an AppContainer process | `E_ACCESSDENIED` |
| Requested integrity level > caller's integrity level | `E_ACCESSDENIED` |
| Unresolvable capability name | `ERROR_NOT_FOUND` |

---

## Requirements

| Requirement | Value |
|---|---|
| **DLL** | processmodel.dll |
| **Minimum supported client** | Windows 11 (experimental) |
| **Header** | Not publicly available (use `GetProcAddress`) |

---

## See Also

- [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw)
- [**CreateProcessAsUser**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasuserw)
- [AppContainer Isolation](/windows/win32/secauthz/appcontainer-isolation)
