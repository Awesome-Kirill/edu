(ns calculate-average)

(defn find-average
  [numbers]
    (/(reduce + numbers)
    (count numbers))
)
