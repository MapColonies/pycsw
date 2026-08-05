# Changelog

## [7.0.0](https://github.com/MapColonies/pycsw/compare/v6.7.3...v7.0.0) (2026-08-05)


### ⚠ BREAKING CHANGES

* create unified chart ([#122](https://github.com/MapColonies/pycsw/issues/122))

### Helm Changes

* create unified chart ([#122](https://github.com/MapColonies/pycsw/issues/122)) ([bd905fb](https://github.com/MapColonies/pycsw/commit/bd905fbf22512e292b12444a97b194ca4051db47))
* remove individual charts ([#125](https://github.com/MapColonies/pycsw/issues/125)) ([0e45b86](https://github.com/MapColonies/pycsw/commit/0e45b864692da3c129bd3db30f89e936ba07913a))

## [6.7.3](https://github.com/MapColonies/pycsw/compare/v6.7.2...v6.7.3) (2026-08-05)


### Helm Changes

* update ngixn version ([#131](https://github.com/MapColonies/pycsw/issues/131)) ([db07c1a](https://github.com/MapColonies/pycsw/commit/db07c1a1c28ebee29bb71d88f40b686607f0d87c))

## [6.7.2](https://github.com/MapColonies/pycsw/compare/v6.7.1...v6.7.2) (2026-08-03)


### Bug Fixes

* raster log scraping typo (MAPCO-11293) ([#128](https://github.com/MapColonies/pycsw/issues/128)) ([1e24d81](https://github.com/MapColonies/pycsw/commit/1e24d81082c785202da9cef4c4cd0e20a06fad06))

## [6.7.1](https://github.com/MapColonies/pycsw/compare/v6.7.0...v6.7.1) (2026-07-22)


### Helm Changes

* remove unncessary config files ([#121](https://github.com/MapColonies/pycsw/issues/121)) ([0043503](https://github.com/MapColonies/pycsw/commit/00435038b2beaae79f0ca845b08e3466abbd8fd3))

## [6.7.0](https://github.com/MapColonies/pycsw/compare/v6.6.1...v6.7.0) (2026-07-16)


### Features

* **helm:** upgrade raster nginx chart dep and image to 2.2.1 ([#123](https://github.com/MapColonies/pycsw/issues/123)) ([38ccdcc](https://github.com/MapColonies/pycsw/commit/38ccdcc3e972dea3a6d73b097fe6836e0981fd43))

## [6.6.1](https://github.com/MapColonies/pycsw/compare/v6.6.0...v6.6.1) (2026-06-24)


### Helm Changes

* upgrade nginx version (MAPCO-10878) ([#119](https://github.com/MapColonies/pycsw/issues/119)) ([37d9a19](https://github.com/MapColonies/pycsw/commit/37d9a19530c376980cea1eda12f43047aa643816))

## [6.6.0](https://github.com/MapColonies/pycsw/compare/v6.5.0...v6.6.0) (2026-06-21)


### Features

* add productSubType to 3d ([#117](https://github.com/MapColonies/pycsw/issues/117)) ([a4542b0](https://github.com/MapColonies/pycsw/commit/a4542b04b5052ab45dfaa815a1ea97a5705a2ab2))

## [6.5.0](https://github.com/MapColonies/pycsw/compare/v6.4.2...v6.5.0) (2026-05-31)


### Features

* add vertical metadata mappings to dem and remove geoid model ([#114](https://github.com/MapColonies/pycsw/issues/114)) ([3f38e70](https://github.com/MapColonies/pycsw/commit/3f38e703dc5a7b877c078c8e92e3e2192d1bb908))

## [6.4.2](https://github.com/MapColonies/pycsw/compare/v6.4.1...v6.4.2) (2026-05-27)


### Helm Changes

* upgrade nginx version and refactor configuration files tosupport nginx extensions( MAPCO-10120) ([#113](https://github.com/MapColonies/pycsw/issues/113)) ([8d97c67](https://github.com/MapColonies/pycsw/commit/8d97c6743053821ad451a5cf3ee6e3482200e28d))

## [6.4.1](https://github.com/MapColonies/pycsw/compare/v6.4.0...v6.4.1) (2026-01-19)


### Bug Fixes

* added stable-sort key for raster helm ([#112](https://github.com/MapColonies/pycsw/issues/112)) ([4b9de6a](https://github.com/MapColonies/pycsw/commit/4b9de6aca735087f26635f72939d62f098378dc9))
* **repository:** Ensure all filters are wrapped (MAPCO-8533) ([#101](https://github.com/MapColonies/pycsw/issues/101)) ([74a8b1d](https://github.com/MapColonies/pycsw/commit/74a8b1dc57b58d019b44592e30ec0acc2e6c4f1f))

## [6.4.0](https://github.com/MapColonies/pycsw/compare/v6.3.1...v6.4.0) (2026-01-06)


### Features

* define new DEM Profile in DEM pycsw repo (MAPCO-8934) ([#105](https://github.com/MapColonies/pycsw/issues/105)) ([581c93e](https://github.com/MapColonies/pycsw/commit/581c93e7f156bb3a3c967be60c12d776b70efcff))
* revert and modify dem (MAPCO-8934) ([#109](https://github.com/MapColonies/pycsw/issues/109)) ([5f1288c](https://github.com/MapColonies/pycsw/commit/5f1288c1a93d85f4f1362ba4d1f2e0bf545a6e7a))

## [6.3.1](https://github.com/MapColonies/pycsw/compare/v6.3.0...v6.3.1) (2026-01-01)


### Bug Fixes

* remove image tag from 3d helm (MAPCO-9268) ([#106](https://github.com/MapColonies/pycsw/issues/106)) ([830d7e7](https://github.com/MapColonies/pycsw/commit/830d7e7e50b60d2c1105d96b74d6cf07d7fe59d8))

## [6.3.0](https://github.com/MapColonies/pycsw/compare/v6.2.2...v6.3.0) (2025-12-18)


### Features

* **repository:** Add option for stable sort (MAPCO-8487) ([#102](https://github.com/MapColonies/pycsw/issues/102)) ([03b54c0](https://github.com/MapColonies/pycsw/commit/03b54c016fcb0b2a7f237edefe1c86dfe5c0116c))


### Helm Changes

* infra labels and annotations in raster pycsw MAPCO-9060 ([#87](https://github.com/MapColonies/pycsw/issues/87)) ([13f5ab6](https://github.com/MapColonies/pycsw/commit/13f5ab692a0f80865d7b449ec136cdc94d163187))

## [6.2.2](https://github.com/MapColonies/pycsw/compare/v6.2.1...v6.2.2) (2025-09-15)


### Dependency Updates

* update mc labels package ([#99](https://github.com/MapColonies/pycsw/issues/99)) ([77a8ffe](https://github.com/MapColonies/pycsw/commit/77a8ffe9d6a7b03a84d9ecfd5c1dbc5a139c94d0))

## [6.2.1](https://github.com/MapColonies/pycsw/compare/v6.2.0...v6.2.1) (2025-08-31)


### Bug Fixes

* set default helm value cors behavior ([#96](https://github.com/MapColonies/pycsw/issues/96)) ([c8dc178](https://github.com/MapColonies/pycsw/commit/c8dc178fb219baf3a93e87bb15a31dbba606ea3f))


### Helm Changes

* 3D helm add mc labels and annotations package (MAPCO-8035) ([#97](https://github.com/MapColonies/pycsw/issues/97)) ([22d4df5](https://github.com/MapColonies/pycsw/commit/22d4df5df476cb893b6a4b52e4c9a95774a0a43e))

## [6.2.0](https://github.com/MapColonies/pycsw/compare/v6.1.0...v6.2.0) (2025-08-21)


### Features

* 3D set default max-records to 50 and fix filterProductStatus filter (MAPCO-8216) ([#92](https://github.com/MapColonies/pycsw/issues/92)) ([6144d68](https://github.com/MapColonies/pycsw/commit/6144d6853f610ad2d100b005fd67bffd744fe9fe))


### Bug Fixes

* docker build issues (MAPCO-8478, MAPCO-7127) ([#91](https://github.com/MapColonies/pycsw/issues/91)) ([25400be](https://github.com/MapColonies/pycsw/commit/25400bed43a04d1fb55ce07c9cfd63a0f745cce9))
* wrong DB queries generated while nesting logical operators (AND, OR) (MAPCO-3141) ([#93](https://github.com/MapColonies/pycsw/issues/93)) ([7139546](https://github.com/MapColonies/pycsw/commit/7139546c2b06b6eb3518b04aa659ce51a2c2f6ca))

## [6.1.0](https://github.com/MapColonies/pycsw/compare/v6.0.1...v6.1.0) (2025-07-31)


### Features

* add 3D helm to pycsw (MAPCO-8216) ([#88](https://github.com/MapColonies/pycsw/issues/88)) ([93e48ae](https://github.com/MapColonies/pycsw/commit/93e48ae80af493043915ef2fdd9e16e710e514b9))


### Helm Changes

* chart version upgraded to 6.0.1 ([#86](https://github.com/MapColonies/pycsw/issues/86)) ([9eb45af](https://github.com/MapColonies/pycsw/commit/9eb45af31104464ed945bf7e6e14b74386f37c2f))
