# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Better logdir creation for different workflows.

## [1.0.22] - 2024-12-31
### Fixed
- Handle chained callbacks in with_choice

## [1.0.21] - 2024-12-31
### Fixed
- Fixed default for with_choice when convert is not set.

### Added
- Add a `clobber` argument to touch.

## [1.0.20] - 2024-12-31
### Fixed
- Add convert_choice to api

## [1.0.19] - 2024-12-30
### Added
- Plotting utility functions

### Fixed
- Update stdout/stderr keys for jobmon again

## [1.0.18] - 2024-12-30
### Fixed
- Update stdout/stderr keys for jobmon

## [1.0.17] - 2024-12-30
### Fixed
- Add invalid choice handling to `convert_choice`.

## [1.0.16] - 2024-12-30
### Fixed
- Use `Collection` instead of `Sequence` in typing to support, e.g., dicts.

## [1.0.15] - 2024-12-28
### Added
- Rework both parallel interfaces to have more flexible types.

## [1.0.14] - 2024-12-28
### Fixed
- Add `with_overwrite` to interface.

## [1.0.13] - 2024-12-28
### Added
- Automatically process choices with a `RUN_ALL` option into a list.
- Add `with_overwrite` cli option.

## [1.0.12] - 2024-11-13
### Fixed
- Return workflow status from `jobmon.run_parallel`

## [1.0.11] - 2024-06-25
### Added
- Backwards compatibility with pandas 1.5

## [1.0.10] - 2024-05-28
### Added
- Change default timeout for jobmon workflow to 3 days instead of 10 hours.

## [1.0.9] - 2024-05-27
### Added
- Add concurrency limit and max attempts to jobmon.

## [1.0.8] - 2024-05-22
### Added
- Proper usage of jobmon node, task, and op args.
- Upgrade `requests` package to patch security vulnerability.

## [1.0.7] - 2024-05-15
### Fixed
- Make output and error log subdirectories

## [1.0.6] - 2024-05-13
### Fixed
- Argument formatting error for click.

## [1.0.5] - 2024-05-13
### Fixed
- Add `RUN_ALL` and `ClickOption` to the `cli_tools` interface.

## [1.0.4] - 2024-05-13
### Changed
- Remove `with_year` and add more generic `with_choice` option to `cli_tools` subpackage.
- Add `process_choice` and `with_choice` to the `cli_tools` interface.

## [1.0.3] - 2024-05-13
### Added
- Add a method to process choice-type CLI options and add a `with_year` option.

## [1.0.2] - 2024-05-10
### Fixed
- Extraneous output-dir arg in jobmon command template

## [1.0.1] - 2024-05-10
### Added
- Basic import test

### Fixed
- Typing of index in `rra_tools.parallel`

## [1.0.0] - 2024-05-09
### Added
- Initial repo setup
- Added translation module
- Added module with shell tools
- Added module for parallel processing with multiprocessing
- Added module for parallel processing with jobmon
- Added subpackage with cli tools
- Added subpackage with logging utilities

[Unreleased]: https://github.com/ihmeuw/rra-tools/compare/1.0.22...master
[1.0.22]: https://github.com/ihmeuw/rra-tools/compare/1.0.21...1.0.22
[1.0.21]: https://github.com/ihmeuw/rra-tools/compare/1.0.20...1.0.21
[1.0.20]: https://github.com/ihmeuw/rra-tools/compare/1.0.19...1.0.20
[1.0.19]: https://github.com/ihmeuw/rra-tools/compare/1.0.18...1.0.19
[1.0.18]: https://github.com/ihmeuw/rra-tools/compare/1.0.17...1.0.18
[1.0.17]: https://github.com/ihmeuw/rra-tools/compare/1.0.16...1.0.17
[1.0.16]: https://github.com/ihmeuw/rra-tools/compare/1.0.15...1.0.16
[1.0.15]: https://github.com/ihmeuw/rra-tools/compare/1.0.14...1.0.15
[1.0.14]: https://github.com/ihmeuw/rra-tools/compare/1.0.13...1.0.14
[1.0.13]: https://github.com/ihmeuw/rra-tools/compare/1.0.12...1.0.13
[1.0.12]: https://github.com/ihmeuw/rra-tools/compare/1.0.11...1.0.12
[1.0.11]: https://github.com/ihmeuw/rra-tools/compare/1.0.10...1.0.11
[1.0.10]: https://github.com/ihmeuw/rra-tools/compare/1.0.9...1.0.10
[1.0.9]: https://github.com/ihmeuw/rra-tools/compare/1.0.8...1.0.9
[1.0.8]: https://github.com/ihmeuw/rra-tools/compare/1.0.7...1.0.8
[1.0.7]: https://github.com/ihmeuw/rra-tools/compare/1.0.6...1.0.7
[1.0.6]: https://github.com/ihmeuw/rra-tools/compare/1.0.5...1.0.6
[1.0.5]: https://github.com/ihmeuw/rra-tools/compare/1.0.4...1.0.5
[1.0.4]: https://github.com/ihmeuw/rra-tools/compare/1.0.3...1.0.4
[1.0.3]: https://github.com/ihmeuw/rra-tools/compare/1.0.2...1.0.3
[1.0.2]: https://github.com/ihmeuw/rra-tools/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/ihmeuw/rra-tools/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/ihmeuw/rra-tools/tree/1.0.0
