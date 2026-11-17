---
title: "WESP boot driver events"
description: "Windows endpoint security platform API reference for boot driver events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_BOOT_LOAD_DRIVER_CONFIG
- ESP_BOOT_LOAD_DRIVER_PARAMETERS
---

# Boot driver events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Boot driver loading

### ESP_BOOT_LOAD_DRIVER_CONFIG

The structure `ESP_BOOT_LOAD_DRIVER_CONFIG` specifies configuration for a boot load driver event.

#### Syntax

```cpp
typedef struct ESP_BOOT_LOAD_DRIVER_CONFIG
{
    ESP_INTEGER_CONFIG ImageFlagsConfig;
    ESP_PATH_CONFIG ImagePathConfig;
    ESP_PATH_CONFIG RegistryPathConfig;
    ESP_STRING_CONFIG CertificatePublisherConfig;
    ESP_STRING_CONFIG CertificateIssuerConfig;
    ESP_INTEGER_CONFIG ImageHashSizeConfig;
    ESP_BINARY_CONFIG ImageHashConfig;
    ESP_INTEGER_CONFIG CertificateThumbprintSizeConfig;
    ESP_BINARY_CONFIG CertificateThumbprintConfig;
    ESP_INTEGER_CONFIG ImageHashAlgorithmConfig;
    ESP_INTEGER_CONFIG ThumbprintHashAlgorithmConfig;
} ESP_BOOT_LOAD_DRIVER_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ImageFlagsConfig | Specifies configuration for the image flags. |
| ImagePathConfig | Specifies configuration for the image path. |
| RegistryPathConfig | Specifies configuration for the registry path. |
| CertificatePublisherConfig | Specifies configuration for the certificate publisher. |
| CertificateIssuerConfig | Specifies configuration for the certificate issuer. |
| ImageHashSizeConfig | Specifies configuration for the image hash size. |
| ImageHashConfig | Specifies configuration for the image hash. |
| CertificateThumbprintSizeConfig | Specifies configuration for the certificate thumbprint size. |
| CertificateThumbprintConfig | Specifies configuration for the certificate thumbprint. |
| ImageHashAlgorithmConfig | Specifies configuration for the image hash algorithm. |
| ThumbprintHashAlgorithmConfig | Specifies configuration for the thumbprint hash algorithm. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_CONFIG`](wesp-rule-value-configuration.md#esp_binary_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_PATH_CONFIG`](wesp-rule-value-configuration.md#esp_path_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BOOT_LOAD_DRIVER_PARAMETERS

The structure `ESP_BOOT_LOAD_DRIVER_PARAMETERS` specifies parameters for the boot load driver event.

#### Syntax

```cpp
typedef struct ESP_BOOT_LOAD_DRIVER_PARAMETERS
{
    UINT32 ImageFlags;
    ESP_PATH ImagePath;
    ESP_PATH RegistryPath;
    ESP_UNICODE_STRING CertificatePublisher;
    ESP_UNICODE_STRING CertificateIssuer;
    UINT32 ImageHashSize;
    _Field_size_bytes_(ImageHashSize) const void* ImageHash;
    UINT32 CertificateThumbprintSize;
    _Field_size_bytes_(CertificateThumbprintSize) const void* CertificateThumbprint;
    UINT32 ImageHashAlgorithm;
    UINT32 ThumbprintHashAlgorithm;
} ESP_BOOT_LOAD_DRIVER_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ImageFlags | Flags that describe the image. This is the same as BDCB_IMAGE_INFORMATION::ImageFlags. |
| ImagePath | The boot start driver's image path. |
| RegistryPath | The boot start driver's registry key path. |
| CertificatePublisher | The publisher of the image's certificate. If the image is not signed, the string is empty. |
| CertificateIssuer | The issuer of the image's certificate. If the image is not signed, the string is empty. |
| ImageHashSize | The size in bytes of the image hash. |
| ImageHash | The Authenticode hash of the image. |
| CertificateThumbprintSize | The size in bytes of the certificate thumbprint. |
| CertificateThumbprint | The hash of the certificate of the signer to be signed. |
| ImageHashAlgorithm | The algorithm of the image hash. This is the same as BDCB_IMAGE_INFORMATION::ImageHashAlgorithm. |
| ThumbprintHashAlgorithm | The algorithm of the certificate thumbprint. This is the same as BDCB_IMAGE_INFORMATION::ThumbprintHashAlgorithm. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PATH`](wesp-common-utilities.md#esp_path)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
