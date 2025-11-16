@echo off
echo ================================================================================
echo APEX 3.0 - QUICK VERIFICATION TEST
echo ================================================================================
echo.
echo This will verify your APEX 3.0 installation in 30 seconds.
echo.
echo Requirements Check:
echo - Windows 10/11 (64-bit)
echo - Python 3.12.x
echo - Internet connection (for NumPy)
echo.
pause
echo.
echo Installing dependencies...
pip install numpy>=2.0.0 --quiet
echo.
echo Running verification test (seed 42)...
echo.
python apex_runner.py --seed 42
echo.
echo ================================================================================
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✓✓✓ VERIFICATION COMPLETE ✓✓✓
    echo.
    echo If you saw "Status: PASS" above, your installation is working correctly!
    echo.
    echo Expected Results for Seed 42:
    echo - Final REI: ~7.01
    echo - Growth: ~133.82%%
    echo - Status: PASS
    echo.
    echo Next Steps:
    echo - Read QUICK_START.txt for complete usage guide
    echo - Try: python apex_runner.py --seeds 42 123 456
    echo.
) else (
    echo.
    echo ✗✗✗ VERIFICATION FAILED ✗✗✗
    echo.
    echo Please check QUICK_START.txt TROUBLESHOOTING section
    echo.
)
echo ================================================================================
echo.
pause
