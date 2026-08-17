---
description: PowerSnap events record interval-based power telemetry on Windows, capturing device state, component power, CPU, thermal, fan activity, and app-attributed energy.
title: PowerSnap events
ms.topic: concept-article
ms.date: 06/11/2026
---

# PowerSnap events

PowerSnap is a form of power telemetry that records how a Windows device uses energy over an interval of time, rather than at a single moment.

When a device drains its battery faster than expected or stays active when it should be idle, you need to see how its power behavior changed over time to find the cause. PowerSnap events give you that interval-level view. This article explains how PowerSnap events behave and what their payload contains, so you can use them for power diagnostics.

## How PowerSnap events fire and cover intervals

The `Microsoft.Windows.SRUM.Telemetry` provider emits PowerSnap events. Each event provides a snapshot of power-related state over an interval, rather than only at a single point in time.

PowerSnap events can fire on device power state transitions and from a timer while a session is active. This behavior lets power diagnostics correlate changes in battery level, component power, CPU residency, thermal state, fan activity, and app-attributed energy with the time range of a user-visible session.

The interval is typically 15 minutes for screen-on sessions, but can be shorter if a trigger occurs, such as an AC/DC transition, Energy Saver turning on or off, or the device going to sleep. For screen-off/sleep/hibernate sessions, one event fires for the entire session at the end of the session, so these sessions can be much longer than 15 minutes. Intervals under 2 minutes don't fire, and Windows appends their data to the next event.

Diagnostic and trace analysis experiences use PowerSnap data to correlate power-related state with a time interval.

## PowerSnap event payload

The PowerSnap event payload can include the following groups of metrics. Not every metric is available on every system or Windows version.

### Metadata

Identifies the event and describes the interval, device state, and battery state it covers.

| Metric | Description |
| --- | --- |
| `EventVersion` | PowerSnap event payload version. |
| `CurrentTimeStamp` | Timestamp when the PowerSnap event was logged. |
| `LastLoggedEventTimeStamp` | Timestamp of the previous logged PowerSnap event. |
| `IntervalStartTimeStamp` | Timestamp when the PowerSnap interval began. |
| `IgnoredEventsCount` | Number of short intervals that were skipped and merged into this event. |
| `IntervalDurationInSeconds` | Length of the PowerSnap interval, in seconds. |
| `IsMonitorOn` | Whether the monitor was on for the interval. |
| `IsDC` | Whether the system was running on battery power. |
| `IsEnergySaverOn` | Whether Energy Saver was active. |
| `SessionType` | Power session type associated with the interval. |
| `ExternalDisplayCount` | Number of connected external displays. |
| `PreviousBatteryPerMyriad` | Battery charge at the start of the interval, in per-myriad (per 10,000) units. |
| `CurrentBatteryPerMyriad` | Battery charge at the end of the interval, in per-myriad units. |
| `PreviousBatteryRemainingCapacitymWh` | Remaining battery capacity at the start of the interval, in milliwatt-hours. |
| `CurrentBatteryRemainingCapacitymWh` | Remaining battery capacity at the end of the interval, in milliwatt-hours. |
| `PreviousMaxBatteryCapacitymWh` | Maximum battery capacity reported at the start of the interval, in milliwatt-hours. |
| `CurrentMaxBatteryCapacitymWh` | Maximum battery capacity reported at the end of the interval, in milliwatt-hours. |
| `BatteryDesignCapacitymWh` | Battery design capacity, in milliwatt-hours. |
| `CurrentInstantaneousPowerMode` | Instantaneous power mode recorded for the interval. |
| `PowerModeChangedInSession` | Whether the effective power mode changed during the containing session. |
| `LastScreenOnSessionGuid` | Identifier for the related screen-on session. |

### Power

Reports component power draw and the number of power samples collected during the interval.

| Metric | Description |
| --- | --- |
| `TotalPowerInMilliWatts` | Total platform battery drain power for the interval, in milliwatts. |
| `CpuPowerInMilliWatts` | CPU core power for the interval, in milliwatts. |
| `PackagePowerInMilliWatts` | Processor package power for the interval, in milliwatts. |
| `GpuPowerInMilliWatts` | GPU power for the interval, in milliwatts. |
| `NpuPowerInMilliWatts` | NPU power for the interval, in milliwatts. |
| `EmiPowerInMilliWatts` | Energy Metering Interface channel power, in milliwatts per channel. |
| `CpuPowerSamples` | CPU power samples collected inside the interval. |
| `GpuPowerSamples` | GPU power samples collected inside the interval. |
| `PackagePowerSamples` | Processor package power samples collected inside the interval. |

### CPU power management

Describes core cycles, idle time, and idle and concurrency residency distributions across big and little cores.

| Metric | Description |
| --- | --- |
| `BigTotalCycles` | Processor cycles recorded on big, or high-performance, cores. |
| `LittleTotalCycles` | Processor cycles recorded on little, or high-efficiency, cores. |
| `AllTotalIdleTime` | Idle time recorded across all cores, in microseconds. |
| `BigTotalIdleTime` | Idle time recorded for big cores, in microseconds. |
| `LittleTotalIdleTime` | Idle time recorded for little cores, in microseconds. |
| `PackageIdleAllIntervalHistogram` | Distribution of all-core idle interval lengths. |
| `PackageIdleBigIntervalHistogram` | Distribution of big-core idle interval lengths. |
| `PackageIdleLittleIntervalHistogram` | Distribution of little-core idle interval lengths. |
| `PackageIdleAllIntervalCumulative` | Cumulative distribution of all-core idle interval lengths. |
| `PackageIdleBigIntervalCumulative` | Cumulative distribution of big-core idle interval lengths. |
| `PackageIdleLittleIntervalCumulative` | Cumulative distribution of little-core idle interval lengths. |
| `AllCoresConcurrencyHistogram` | Distribution of the number of concurrently active cores. |
| `BigCoresConcurrencyHistogram` | Distribution of concurrently active big cores. |
| `LittleCoresConcurrencyHistogram` | Distribution of concurrently active little cores. |
| `AllCoresConcurrencyCumulative` | Cumulative distribution of all-core concurrency. |
| `BigCoresConcurrencyCumulative` | Cumulative distribution of big-core concurrency. |
| `LittleCoresConcurrencyCumulative` | Cumulative distribution of little-core concurrency. |
| `CStateHistogram` | Package C-state residency distribution. |
| `CStateCumulative` | Cumulative package C-state residency distribution. |

### P-state histograms

Captures processor frequency (P-state) residency by quality of service (QoS) class and core type, as both interval and cumulative distributions.

| Metric | Description |
| --- | --- |
| `PStatesBigHighQosHistogram` | Frequency residency for high-QoS work on big cores. |
| `PStatesLittleHighQosHistogram` | Frequency residency for high-QoS work on little cores. |
| `PStatesBigLowQosHistogram` | Frequency residency for low-QoS work on big cores. |
| `PStatesLittleLowQosHistogram` | Frequency residency for low-QoS work on little cores. |
| `PStatesBigTotalHistogram` | Total frequency residency for big cores. |
| `PStatesLittleTotalHistogram` | Total frequency residency for little cores. |
| `PStatesBigHighQosCumulative` | Cumulative high-QoS frequency residency for big cores. |
| `PStatesLittleHighQosCumulative` | Cumulative high-QoS frequency residency for little cores. |
| `PStatesBigLowQosCumulative` | Cumulative low-QoS frequency residency for big cores. |
| `PStatesLittleLowQosCumulative` | Cumulative low-QoS frequency residency for little cores. |
| `PStatesBigTotalCumulative` | Cumulative total frequency residency for big cores. |
| `PStatesLittleTotalCumulative` | Cumulative total frequency residency for little cores. |

### Thermal

Reports time spent at each thermal signal or threshold, plus a temperature readout when available.

| Metric | Description |
| --- | --- |
| `THERMAL_STATUS` (Index 0) | Time with a thermal status signal, in seconds. |
| `THERMAL_PROC_HOT` (Index 1) | Time with processor hot asserted, in seconds. |
| `THERMAL_CRITICAL_TEMP` (Index 2) | Time at a critical thermal condition, in seconds. |
| `THERMAL_THRESHOLD_1` (Index 3) | Time at thermal threshold 1, in seconds. |
| `THERMAL_THRESHOLD_2` (Index 4) | Time at thermal threshold 2, in seconds. |
| `THERMAL_POWER_LIMITATION` (Index 5) | Time under thermal power limitation, in seconds. |
| `THERMAL_READOUT` (Index 6) | Thermal readout in degrees Celsius, when available. |

### Fan

Describes fan on-time and the distribution of fan activity across noise and impact buckets.

| Metric | Description |
| --- | --- |
| `FanOnTotalTimeInSeconds` | Total time the fan was on during the interval, in seconds. |
| `FanImpactNoiseHistogram` | Distribution of fan time by fan impact or noise bucket. |
| `FanImpactNoiseCumulative` | Cumulative distribution of fan impact or noise buckets. |
| `FanImpactZonesHistogram` | Distribution of fan time by impact zone. |
| `FanImpactZonesCumulative` | Cumulative distribution of fan impact zones. |
| `FanRpmBucketBoundaries` | RPM boundaries for fan buckets. |
| `FanImpactZonesBoundaries` | RPM boundaries for fan impact zones. |

### App power attribution (E3)

The Energy Estimation Engine (E3) attributes interval energy to apps, display, GPU, and other categories, including energy merged from skipped intervals.

| Metric | Description |
| --- | --- |
| `TotalAppEnergySessionInMilliJoules` | Total app-attributed energy in the interval, in millijoules. |
| `TotalAppEnergyMissedSessionsInMilliJoules` | App-attributed energy from skipped intervals, merged into this event, in millijoules. |
| `TotalDisplayEnergySessionInMilliJoules` | Display-attributed app energy in the interval, in millijoules. |
| `TotalDisplayEnergyMissedSessionsInMilliJoules` | Display-attributed app energy from skipped intervals, in millijoules. |
| `TotalGpuEnergyInMilliJoules` | GPU energy attributed by E3 in the interval, in millijoules. |
| `TotalGpuEnergyMissedSessionsInMilliJoules` | GPU energy from skipped intervals, in millijoules. |
| `TotalLossEnergyInMilliJoules` | E3 loss energy for the interval, in millijoules. |
| `TotalOtherEnergyInMilliJoules` | E3 other energy for the interval, in millijoules. |
| `TotalUnknownAppEnergyInMilliJoules` | E3 energy attributed to unknown app activity, in millijoules. |
| `UnknownAppDurationInSeconds` | Duration associated with unknown app energy, in seconds. |
| `AttributedToSpecificAppInMyriad` | Share of app energy attributed to named apps, in per-myriad units. |
| `AppEnergyNames` | App or package names for top app-attributed records. |
| `AppEnergySessionInMilliJoules` | Per-app non-display energy in the interval, in millijoules. |
| `AppEnergyMissedSessionsInMilliJoules` | Per-app non-display energy from skipped intervals, in millijoules. |
| `AppDisplayEnergySessionInMilliJoules` | Per-app display energy in the interval, in millijoules. |
| `AppDisplayEnergyMissedSessionsInMilliJoules` | Per-app display energy from skipped intervals, in millijoules. |

## SleepStudy reports

SleepStudy HTML reports can include PowerSnap data when PowerSnap collects events for a session. To generate a report, run `powercfg /sleepstudy` in a terminal. SleepStudy processes the PowerSnap payload for report readability, and the payload is only a subset of all the information PowerSnap collects.

## Notes and limitations

- Field availability varies by Windows version, device platform, processor topology, firmware, and available sensors.
- Some fields can be empty or zero when a platform doesn't expose the corresponding hardware data.
- App names and power attribution can reveal user or workload activity. Treat PowerSnap events and reports that contain PowerSnap data as diagnostic data.

## Related topics

- [Power Management](power-management-portal.md)
- [System power states](system-power-states.md)
- [System Power Management Events](system-power-management-events.md)
