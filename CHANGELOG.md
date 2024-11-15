# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/ihmeuw/rra-tools/compare/1.0.12...master
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
