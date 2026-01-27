---
title: Draft correction — Example C program: Creating a certificate chain (trust status handling)
summary: The sample handles only one CERT_TRUST flag and prints "No error" via else, which suppresses other errors. Trust status is a bitfield and must be checked per-flag; print "No error" only when Status == CERT_TRUST_NO_ERROR.
---

Target page: https://learn.microsoft.com/en-us/windows/win32/seccrypto/example-c-program-creating-a-certificate-chain

Problem
- The example treats `CERT_TRUST_CTL_IS_NOT_VALID_FOR_USAGE` as the sole error and uses `else` to print "No error found".
- `pChainContext->TrustStatus.Status` is a bitfield of `CERT_TRUST_*` flags. Multiple error bits can be set simultaneously, and they must be checked independently.
- "No error found" should be printed only when `Status == CERT_TRUST_NO_ERROR` (0).

Proposed text change
- Replace the single-flag `if ... else` logic with independent bit checks for each relevant error flag.
- Add an initial check for `Status == CERT_TRUST_NO_ERROR` to print the no-error message.
- Optionally report `TrustStatus.InfoStatus` for non-error diagnostics.

Proposed code correction (drop-in pattern)
```c
DWORD status = pChainContext->TrustStatus.Status;
DWORD info   = pChainContext->TrustStatus.InfoStatus;

if (status == CERT_TRUST_NO_ERROR) {
    puts("No error found for this certificate or chain.");
} else {
    if (status & CERT_TRUST_IS_NOT_TIME_VALID)
        puts("Certificate or chain is not time valid.");
    if (status & CERT_TRUST_IS_NOT_SIGNATURE_VALID)
        puts("Signature is not valid.");
    if (status & CERT_TRUST_IS_REVOKED)
        puts("Certificate or chain is revoked.");
    if (status & CERT_TRUST_IS_NOT_VALID_FOR_USAGE)
        puts("Not valid for the requested usage.");

    // CTL-related flags (when a CTL is involved)
    if (status & CERT_TRUST_CTL_IS_NOT_TIME_VALID)
        puts("CTL time is not valid.");
    if (status & CERT_TRUST_CTL_IS_NOT_SIGNATURE_VALID)
        puts("CTL signature is not valid.");
    if (status & CERT_TRUST_CTL_IS_NOT_VALID_FOR_USAGE)
        puts("CTL is not valid for usage.");

    // (Add other checks as needed based on application requirements)
}

// Optional: informational diagnostics
if (info & CERT_TRUST_HAS_EXACT_MATCH_ISSUER)
    puts("Exact-match issuer found.");
// ...etc.
```

Rationale
- All trust status codes are bitflags; multiple errors can co-exist. Using `else` to print "No error" after checking a single flag will incorrectly hide other errors.
- This pattern ensures each set bit is reported and avoids false "No error" messages.

Notes
- Consider including additional commonly-checked flags per `CERT_TRUST_*` definitions if relevant to the sample scope.
- Minor typo in existing sample string: "hain" → "chain".

Impact
- Corrects error reporting in the sample and prevents misleading "No error" output in the presence of other trust failures.
