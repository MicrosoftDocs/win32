---
title: "WESP transaction events"
description: "Windows endpoint security platform API reference for transaction events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_KTM_TRANSACTION_COMMIT_CONFIG
- ESP_KTM_TRANSACTION_COMMIT_PARAMETERS
- ESP_KTM_TRANSACTION_ROLLBACK_CONFIG
- ESP_KTM_TRANSACTION_ROLLBACK_PARAMETERS
---

# Transaction events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Transaction commit

### ESP_KTM_TRANSACTION_COMMIT_CONFIG

The structure `ESP_KTM_TRANSACTION_COMMIT_CONFIG` is used to configure a KTM transaction commit event.

#### Syntax

```cpp
typedef struct ESP_KTM_TRANSACTION_COMMIT_CONFIG
{
    ESP_KTM_TRANSACTION_CONFIG TransactionConfig;
} ESP_KTM_TRANSACTION_COMMIT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| TransactionConfig | Specifies configuration for the KTM transaction. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_KTM_TRANSACTION_CONFIG`](wesp-other-event-objects.md#esp_ktm_transaction_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_KTM_TRANSACTION_COMMIT_PARAMETERS

The structure `ESP_KTM_TRANSACTION_COMMIT_PARAMETERS` contains the parameters associated with a KTM transaction commit event notification.

#### Syntax

```cpp
typedef struct ESP_KTM_TRANSACTION_COMMIT_PARAMETERS
{
    ESP_KTM_TRANSACTION_INFO Transaction;
} ESP_KTM_TRANSACTION_COMMIT_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Transaction | The KTM transaction that is being committed. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_KTM_TRANSACTION_INFO`](wesp-other-event-objects.md#esp_ktm_transaction_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Transaction rollback

### ESP_KTM_TRANSACTION_ROLLBACK_CONFIG

The structure `ESP_KTM_TRANSACTION_ROLLBACK_CONFIG` is used to configure a KTM transaction rollback event.

#### Syntax

```cpp
typedef struct ESP_KTM_TRANSACTION_ROLLBACK_CONFIG
{
    ESP_KTM_TRANSACTION_CONFIG TransactionConfig;
} ESP_KTM_TRANSACTION_ROLLBACK_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| TransactionConfig | Specifies configuration for the KTM transaction. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_KTM_TRANSACTION_CONFIG`](wesp-other-event-objects.md#esp_ktm_transaction_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_KTM_TRANSACTION_ROLLBACK_PARAMETERS

The structure `ESP_KTM_TRANSACTION_ROLLBACK_PARAMETERS` contains the parameters associated with a KTM transaction rollback event notification.

#### Syntax

```cpp
typedef struct ESP_KTM_TRANSACTION_ROLLBACK_PARAMETERS
{
    ESP_KTM_TRANSACTION_INFO Transaction;
} ESP_KTM_TRANSACTION_ROLLBACK_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Transaction | The KTM transaction that is being rolled back. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_KTM_TRANSACTION_INFO`](wesp-other-event-objects.md#esp_ktm_transaction_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
