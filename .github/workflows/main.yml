name: Build APK
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Build with Buildozer
        uses: ArtemGr/buildozer-action@v1
        with:
          command: buildozer android debug
          buildozer_version: master
