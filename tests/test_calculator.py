from calculator import estimate_band_size

def test_estimate():
    ladder_sizes = [10000, 8000, 6000, 4000]
    ladder_distances = [10, 15, 20, 25]
    sample_distance = 18

    result = estimate_band_size(ladder_sizes, ladder_distances, sample_distance)

    assert result > 0
