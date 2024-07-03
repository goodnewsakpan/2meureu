import styles from './CourseDashboard.module.css'
import CourseSidebar from "../components/CourseSidebar";
import CourseBoard from '../components/CourseBoard';

export default function CourseDashboard() {
  return (
    <header className={styles.header}>
        <CourseSidebar />
        <CourseBoard />
    </header>
  )
}
